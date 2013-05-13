'''
Created on 22 Mar 2013
Test suite for Match

@author: Javi Carretero
'''
from com.jc.exception import *
from com.jc.match import Match
from com.jc.player import Player
import unittest

class MatchTest(unittest.TestCase):
    
    def setUp(self):
        self.match = Match()
        self.p1 = Player("name1","surname1",None,1)
        self.p2 = Player("name2","surname2",None,2)
        
    def test_newMatch(self):
        self.assertRaises(PlayerNumberError, self.match.startMatch)
        
    def test_noMoreThan2Players(self):
        self.match.addPlayers([self.p1,self.p2])
        p3 = Player("name3","surname3",None,3)
        self.assertRaises(NoMorePlayersError, self.match.addPlayers,p3)
        
    def test_NoRestartsAllowed(self):
        self.match.addPlayers([self.p1,self.p2])
        self.match.startMatch()
        self.assertRaises(MatchAlreadyStartedError, self.match.startMatch)
        
if __name__ == "__main__":
    unittest.main()