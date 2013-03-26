'''
Created on 22 Mar 2013
Tennis Simulation

@author: Javi Carretero
'''
from exception import *
from com.jc.player import Player
from com.jc import CHAMPIONSHIP_MATCH, NORMAL_MATCH
from com.jc.set import Set
from com.jc import Point
import logging
logger = logging.getLogger(__name__)

class Match(Point):
    """Class representing a Match in Tennis"""
    def __init__(self, matchType=NORMAL_MATCH):
        super(Match,self).__init__()
        self.__players = []
        self.__match_type = matchType
        
    def changeMatchType(self, new_match_type):
        if(len(self._scorings) != 0):
            raise MatchAlreadyStartedError()
        self.__match_type = new_match_type
        logger.debug("Match has changed from %s to %s",self.__match_type,new_match_type)
    
    def addPlayers(self, pl):
        if(len(self.__players) == 2):
            raise NoMorePlayersError()
        if(type(pl) is Player):
            self.__players.append(pl)
        elif(type(pl) is list):
            for player in pl:
                self.addPlayers(player)
    
    def startMatch(self):
        if(len(self.__players) != 2):
            raise PlayerNumberError(len(self.__players))
        if(len(self._scorings) != 0):
            raise MatchAlreadyStartedError()
        
        logger.info("The match between %s and %s is about to start!", str(self.__players[0]), str(self.__players[1]))
        logger.debug("The type of the match is %s", self.__match_type)
        self._scorings.append(self._newScoring())
        
    def incrementScore(self, player):
        if(player not in self.__players):
            raise InvalidPlayerError(player)
        if(self._winner is not None):
            raise MatchAlreadyFinishedError()
        super(Match,self).getActualPoint().incrementScore(player)
        if(super(Match,self).getActualPoint().isFinished()):
            setsForPlayer = self.getNumScoringsWon(player)
            if((self.__match_type == CHAMPIONSHIP_MATCH and setsForPlayer == 3)
               or
               (self.__match_type == NORMAL_MATCH and setsForPlayer == 2)):
                logger.info("Match won by %s",str(player))
                self._winner = player
            else:
                self._scorings.append(self._newScoring())
            
    def score(self):
        return map(lambda s: s.score(), self._scorings)
        
    def _newScoring(self):
        return Set(self.__players)
        

