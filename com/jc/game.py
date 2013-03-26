'''
Created on 22 Mar 2013

@author: Javi Carretero
'''
from com.jc import Point
from com.jc.exception import *
from com.jc.point import TennisPoint
import logging
logger = logging.getLogger(__name__)

class Game(Point):
    """Class representing a Game in Tennis"""
    _minPointsToWin = 4
    
    def __init__(self,players):
        super(Game,self).__init__()
        self._scorings.append(self._newScoring())
        self.__players = players
        
    def incrementScore(self,player):
        if(player not in self.__players):
            raise InvalidPlayerError(player)
        if(self._winner is not None):
            raise GameAlreadyFinishedError()
        super(Game,self).getActualPoint().incrementScore(player)
        pointsForPlayer = filter(lambda n: n.isFinished() and n.getWinner() == player, self._scorings)
        pointsAgainstPlayer = filter(lambda n: n.isFinished() and n.getWinner() != player, self._scorings)
        if(len(pointsForPlayer) >= self._minPointsToWin and len(pointsForPlayer) - len(pointsAgainstPlayer) >= 2):
            logger.debug("%s won by %s",self._typeOfGame(),str(player))
            self._winner = player
        else:
            self._scorings.append(self._newScoring())
            
    def score(self, player=None):
        if(player is None):
            player1 = self.__players[0]
            player2 = self.__players[1]
            return self.score(player1) + "-" + self.score(player2)
        if(player not in self.__players):
            raise InvalidPlayerError(player)
        if(self.isFinished() and self.getWinner() == player):
            return "W"
        numGames = self.getNumScoringsWon(player)        
        numGamesOpp = self.getNumScoringsLost(player)
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
        
    def _newScoring(self):
        return TennisPoint()
    
    def _typeOfGame(self):
        return "Game"
    
class TieBreak(Game):
    """Class representing a Tiebreak in Tennis"""
    _minPointsToWin = 7
    
    def __init__(self, players):
        super(TieBreak,self).__init__(players)
    
    def score(self, player=None):
        if(player is None):
            player1 = self.__players[0]
            player2 = self.__players[1]
            return self.score(player1) + "-" + self.score(player2)
        if(player not in self.__players):
            raise InvalidPlayerError(player)
        if(self.isFinished() and self.getWinner() == player):
            return "W"
        
        numGames = self.getNumScoringsWon(player)
        numGamesOpp = self.getNumScoringsLost(player)
        if(numGames <= 6):
            return str(numGames)
        elif(numGames <= numGamesOpp):
            return "6"
        elif(numGames == numGamesOpp + 1):
            return "Adv"
        
    def _typeOfGame(self):
        return "TieBreak"