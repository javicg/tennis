'''
Created on 22 Mar 2013
Tennis Simulation

@author: Javi Carretero
'''
from exception import *
from Player import *
from com.jc import *

class Match(object):
    def __init__(self,matchType):
        self.__players__ = []
        self.__sets__ = []
        self.match_type = matchType
    
    def addPlayer(self, player):
        if(len(self.__players__) == 2):
            raise NoMorePlayersError()
        self.__players__.append(player)
        
    def addPlayers(self, listOfPlayers):
        for player in listOfPlayers:
            self.addPlayer(player)
    
    def startMatch(self):
        if(len(self.__players__) != 2):
            raise PlayerNumberError(len(self.__players__))
        print "The match between",self.__players__[0],"and",self.__players__[1],"is about to start!"
        print "The type of the match is",self.match_type
        #TODO
        
        
if __name__ == "__main__":
    # List of players
    nadal = Player("Rafael","Nadal","Rafa Nadal",4)
    djokovic = Player("Novak","Djokovic","Djokovic",1)
    
    m = Match(CHAMPIONSHIP_MATCH)
    m.addPlayer(nadal)
    m.addPlayer(djokovic)
    
    m.startMatch()