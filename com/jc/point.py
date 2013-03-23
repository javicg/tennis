'''
Created on 22 Mar 2013

@author: Javi Carretero
'''
class Point(object):
    """Class representing a Point in Tennis"""
    def __init__(self):
        self.__winner = None
    
    def declareWinner(self,player):
        self.__winner = player
        
    def isFinished(self):
        return self.__winner is not None
    
    def getWinner(self):
        return self.__winner