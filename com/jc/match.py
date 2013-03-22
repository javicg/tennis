'''
Created on 22 Mar 2013
Tennis Simulation

@author: Javi Carretero
'''
from exception import *
from com.jc.Player import Player
from com.jc import CHAMPIONSHIP_MATCH

class Match(object):
    
    def __init__(self, matchType=CHAMPIONSHIP_MATCH):
        self.__players__ = []
        self.__sets__ = []
        self.__match_type = matchType
        
    def changeMatchType(self, new_match_type):
        self.__match_type = new_match_type
        print "Match has changed from",self.__match_type,"to",new_match_type
    
    def addPlayer(self, pl):
        if(len(self.__players__) == 2):
            raise NoMorePlayersError()
        if(type(pl) is Player):
            self.__players__.append(pl)
        elif(type(pl) is list):
            for player in pl:
                self.addPlayer(player)
    
    def startMatch(self):
        if(len(self.__players__) != 2):
            raise PlayerNumberError(len(self.__players__))
        print "The match between", self.__players__[0], "and", self.__players__[1], "is about to start!"
        print "The type of the match is", self.__match_type
        # TODO

