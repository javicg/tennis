'''
Created on 22 Mar 2013
Tennis Simulation

@author: Javi Carretero
'''
from exception import *
from com.jc.player import Player
from com.jc import CHAMPIONSHIP_MATCH
from com.jc.set import Set

class Match(object):
    """Class representing a Match in Tennis"""
    def __init__(self, matchType=CHAMPIONSHIP_MATCH):
        self.__players = []
        self.__sets = []
        self.__match_type = matchType
        self.__winner = None
        
    def changeMatchType(self, new_match_type):
        if(len(self.__sets) != 0):
            raise MatchAlreadyStartedError()
        self.__match_type = new_match_type
        print "Match has changed from",self.__match_type,"to",new_match_type
    
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
        if(len(self.__sets) != 0):
            raise MatchAlreadyStartedError()
        
        print "The match between", self.__players[0], "and", self.__players[1], "is about to start!"
        print "The type of the match is", self.__match_type
        self.__newSet()
        
    def incrementScore(self, player):
        if(player not in self.__players):
            raise InvalidPlayerError(player)
        if(self.__winner is not None):
            raise MatchAlreadyFinishedError()
        self.getActualSet().incrementScore(player)
        if(self.getActualSet().isFinished()):
            self.__newSet()
            
    def score(self):
        setScore = []
        for set in self.__sets:
            setScore.append(set.score())
        return setScore
        
    def getActualSet(self):
        return self.__sets[len(self.__sets) - 1]
        
    def __newSet(self):
        self.__sets.append(Set(self.__players))
        

