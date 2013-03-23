'''
Created on 22 Mar 2013

@author: Javi Carretero
'''
from com.jc.point import Point
from com.jc.exception import *
import math

class Game(object):
    """Class representing a Game in Tennis"""
    def __init__(self):
        self.__points = []
        self.__points.append(Point())
        self.__winner = None
        
    def getActualPoint(self):
        return self.__points[len(self.__points) - 1]
        
    def incrementScore(self,player):
        if(self.__winner is not None):
            raise GameAlreadyFinished()
        self.getActualPoint().declareWinner(player)
        gamesForPlayer = filter(lambda n: n.isFinished() and n.getWinner() == player, self.__points)
        gamesAgainstPlayer = filter(lambda n: n.isFinished() and n.getWinner() != player, self.__points)
        if(len(gamesForPlayer) >= 4 and len(gamesForPlayer) - len(gamesAgainstPlayer) >= 2):
            print "Game won by",player
            self.__winner = player
        else:
            self.__points.append(Point())
            
    def getWinner(self):
        return self.__winner
            
    def isFinished(self):
        return self.__winner is not None