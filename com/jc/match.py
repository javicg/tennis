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
        
    def changeMatchType(self, new_match_type):
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
            raise MatchAlreadyStarted()
        
        print "The match between", self.__players[0], "and", self.__players[1], "is about to start!"
        print "The type of the match is", self.__match_type
        self.__initialise()
        
    def __initialise(self):
        self.__sets.append(Set())
        

