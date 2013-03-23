'''
Created on 22 Mar 2013

@author: Javi Carretero
'''
from com.jc.game import Game

class Set(object):
    """Class representing a Set in Tennis"""
    def __init__(self):
        self.__games = []
        self.__games.append(Game())
        
    def getActualGame(self):
        return self.__games[len(self.__games) - 1]