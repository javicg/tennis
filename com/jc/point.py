'''
Created on 22 Mar 2013

@author: Javi Carretero
'''
from com.jc import Point

class TennisPoint(Point):
    """Class representing a Point in Tennis"""
    def __init__(self):
        super(TennisPoint,self).__init__()
        
    def incrementScore(self,player):
        self._winner = player
        
    def score(self, player=None):
        if(self._winner is None):
            return "0"
        else:
            if(player is not None and self._winner == player):
                return "W"
            else:
                return "L"