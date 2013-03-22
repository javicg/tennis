'''
Created on 22 Mar 2013
Test suite for Match

@author: Javi
'''
import unittest
from com.jc.exception import *
from com.jc.Match import Match
from com.jc.Player import Player


class MatchTest(unittest.TestCase):
    
    def setUp(self):
        self.match = Match()
        
    def test_newMatch(self):
        self.assertRaises(PlayerNumberError, self.match.startMatch)
        
    def test_noMoreThan2Players(self):
        p1 = Player("name1","surname1",1)
        p2 = Player("name2","surname2",2)
        p3 = Player("name3","surname3",3)
        self.match.addPlayer(p1)
        self.match.addPlayer(p2)
        self.assertRaises(NoMorePlayersError, self.match.addPlayer,p3)
        
if __name__ == "__main__":
    unittest.main()