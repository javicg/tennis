'''
Created on 22 Mar 2013

@author: Javi Carretero
'''
from exception import *
from com.jc.game import Game, TieBreak
from com.jc import Point
import logging
logger = logging.getLogger(__name__)

class Set(Point):
    """Class representing a Set in Tennis"""
    def __init__(self, players):
        super(Set,self).__init__()
        self.__players = players
        self._scorings.append(self._newScoring())
        
    def incrementScore(self, player):
        if(player not in self.__players):
            raise InvalidPlayerError(player)
        if(self._winner is not None):
            raise SetAlreadyFinishedError()
        super(Set,self).getActualPoint().incrementScore(player)
        if(super(Set,self).getActualPoint().isFinished()):
            numGames = self.getNumScoringsWon(player)
            numGamesOpp = self.getNumScoringsLost(player)
            if((numGames >= 6 and numGames >= numGamesOpp + 2)
                or
                (isinstance(super(Set,self).getActualPoint(),TieBreak))):
                logger.debug("Set won by %s",str(player))
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
        return str(self.getNumScoringsWon(player))
    
    def _newScoring(self):
        numGames = self.getNumScoringsWon(self.__players[0])
        numGamesOpp = self.getNumScoringsWon(self.__players[1])
        if(numGames == numGamesOpp == 6):
            logger.debug("Set goes to TieBreak")
            return TieBreak(self.__players)
        else:
            return Game(self.__players)