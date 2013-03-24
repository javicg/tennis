'''
Created on 22 Mar 2013

@author: Javi Carretero
'''
from com.jc.point import Point
from com.jc.exception import *

class Game(object):
    """Class representing a Game in Tennis"""
    _minPointsToWin = 4
    
    def __init__(self,players):
        self.__points = []
        self.__points.append(Point())
        self.__winner = None
        self.__players = players
        
    def getActualPoint(self):
        return self.__points[len(self.__points) - 1]
        
    def incrementScore(self,player):
        if(player not in self.__players):
            raise InvalidPlayerError(player)
        if(self.__winner is not None):
            raise GameAlreadyFinishedError()
        self.getActualPoint().declareWinner(player)
        pointsForPlayer = filter(lambda n: n.isFinished() and n.getWinner() == player, self.__points)
        pointsAgainstPlayer = filter(lambda n: n.isFinished() and n.getWinner() != player, self.__points)
        if(len(pointsForPlayer) >= self._minPointsToWin and len(pointsForPlayer) - len(pointsAgainstPlayer) >= 2):
            print self._typeOfGame(),"won by",player
            self.__winner = player
        else:
            self.__points.append(Point())
            
    def score(self, player=None):
        if(player is None):
            player1 = self.__players[0]
            player2 = self.__players[1]
            return self.score(player1) + "-" + self.score(player2)
        if(player not in self.__players):
            raise InvalidPlayerError(player)
        if(self.isFinished() and self.getWinner() == player):
            return "W"
        pointsForPlayer = filter(lambda n: n.isFinished() and n.getWinner() == player, self.__points)
        numGames = len(pointsForPlayer)
        pointsAgainstPlayer = filter(lambda n: n.isFinished() and n.getWinner() != player, self.__points)
        numGamesOpp = len(pointsAgainstPlayer)
        if(numGames == 0):
            return "0"
        elif(numGames == 1):
            return "15"
        elif(numGames == 2):
            return "30"
        elif(numGames == 3 or numGames <= numGamesOpp):
            return "40"
        elif(numGames == numGamesOpp + 1):
            return "Adv"
            
    def getWinner(self):
        return self.__winner
            
    def isFinished(self):
        return self.__winner is not None
    
    def _typeOfGame(self):
        return "Game"
    
class TieBreak(Game):
    """Class representing a Tiebreak in Tennis"""
    _minPointsToWin = 7
    
    def score(self, player=None):
        if(player is None):
            player1 = self.__players[0]
            player2 = self.__players[1]
            return self.score(player1) + "-" + self.score(player2)
        if(player not in self.__players):
            raise InvalidPlayerError(player)
        if(self.isFinished() and self.getWinner() == player):
            return "W"
        pointsForPlayer = filter(lambda n: n.isFinished() and n.getWinner() == player, self.__points)
        numGames = len(pointsForPlayer)
        pointsAgainstPlayer = filter(lambda n: n.isFinished() and n.getWinner() != player, self.__points)
        numGamesOpp = len(pointsAgainstPlayer)
        
        if(numGames <= 6):
            return str(numGames)
        elif(numGames <= numGamesOpp):
            return "6"
        elif(numGames == numGamesOpp + 1):
            return "Adv"
        
    def _typeOfGame(self):
        return "TieBreak"