'''
Created on 22 Mar 2013
Test suite for Match

@author: Javi Carretero
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
        p1 = Player("name1","surname1",None,1)
        p2 = Player("name2","surname2",None,2)
        p3 = Player("name3","surname3",None,3)
        self.match.addPlayer([p1,p2])
        self.assertRaises(NoMorePlayersError, self.match.addPlayer,p3)
        
if __name__ == "__main__":
    unittest.main()