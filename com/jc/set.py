'''
Created on 22 Mar 2013

@author: Javi Carretero
'''
from exception import *
from com.jc.game import Game, TieBreak

class Set(object):
    """Class representing a Set in Tennis"""
    def __init__(self, players):
        self.__games = []
        self.__players = players
        self.__newGame()
        self.__winner = None
        
    def incrementScore(self, player):
        if(player not in self.__players):
            raise InvalidPlayerError(player)
        if(self.__winner is not None):
            raise SetAlreadyFinishedError()
        self.getActualGame().incrementScore(player)
        if(self.getActualGame().isFinished()):
            gamesForPlayer = filter(lambda n: n.isFinished() and n.getWinner() == player, self.__games)
            numGames = len(gamesForPlayer)
            gamesAgainstPlayer = filter(lambda n: n.isFinished() and n.getWinner() != player, self.__games)
            numGamesOpp = len(gamesAgainstPlayer)
            if((numGames >= 6 and numGames >= numGamesOpp + 2)
                or
                (isinstance(self.getActualGame(),TieBreak))):
                print "Set won by",player
                self.__winner = player
            elif(numGames == numGamesOpp == 6):
                # TieBreak
                self.__newTieBreak()
            else:
                self.__newGame()
                
    def score(self, player=None):
        if(player is None):
            player1 = self.__players[0]
            player2 = self.__players[1]
            return self.score(player1) + "-" + self.score(player2)
        if(player not in self.__players):
            raise InvalidPlayerError(player)
        gamesForPlayer = filter(lambda n: n.isFinished() and n.getWinner() == player, self.__games)
        numGames = len(gamesForPlayer)
        return str(numGames)
        
    def getActualGame(self):
        return self.__games[len(self.__games) - 1]
    
    def getWinner(self):
        return self.__winner
            
    def isFinished(self):
        return self.__winner is not None
    
    def __newGame(self):
        self.__games.append(Game(self.__players))
        
    def __newTieBreak(self):
        print "Set goes to TieBreak!"
        self.__games.append(TieBreak(self.__players))