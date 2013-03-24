'''
Created on 23 Mar 2013
Test suite for Game

@author: Javi Carretero
'''
import unittest
from com.jc.game import Game
from com.jc.player import Player
from com.jc.exception import InvalidPlayerError, GameAlreadyFinishedError

class GameTest(unittest.TestCase):
    
    def setUp(self):
        self.p1 = Player("name1","surname1",None,1)
        self.p2 = Player("name2","surname2",None,2)
        self.game = Game([self.p1,self.p2])
        
    def test_newGame(self):
        self.assertFalse(self.game.isFinished())
        
    def test_winningConditions_beforeDeuce(self):
        self.game.incrementScore(self.p1)
        self.game.incrementScore(self.p1)
        self.game.incrementScore(self.p1)
        self.game.incrementScore(self.p1)
        self.assertTrue(self.game.isFinished())
        self.assertEqual(self.game.getWinner(), self.p1)
        
    def test_winningConditions_afterDeuce(self):
        self.assertTrue(self.game.score() == "0-0")
        self.game.incrementScore(self.p1)
        self.assertTrue(self.game.score() == "15-0")
        self.game.incrementScore(self.p2)
        self.assertTrue(self.game.score() == "15-15")
        self.game.incrementScore(self.p1)
        self.assertTrue(self.game.score() == "30-15")
        self.game.incrementScore(self.p2)
        self.assertTrue(self.game.score() == "30-30")
        self.game.incrementScore(self.p1)
        self.assertTrue(self.game.score() == "40-30")
        self.game.incrementScore(self.p2)
        self.assertTrue(self.game.score() == "40-40") # DEUCE
        self.game.incrementScore(self.p1)
        self.assertTrue(self.game.score() == "Adv-40")
        self.assertFalse(self.game.isFinished()) # Game still on!
        self.game.incrementScore(self.p2)
        self.assertTrue(self.game.score() == "40-40") # DEUCE
        self.game.incrementScore(self.p2)
        self.assertTrue(self.game.score() == "40-Adv")
        self.assertFalse(self.game.isFinished()) # Game still on!
        self.game.incrementScore(self.p2) # p2 wins the Game
        self.assertTrue(self.game.isFinished())
        self.assertEqual(self.game.getWinner(), self.p2)
        self.assertTrue(self.game.score() == "40-W")
        
    def test_gameAlreadyFinished(self):
        self.game.incrementScore(self.p1)
        self.game.incrementScore(self.p1)
        self.game.incrementScore(self.p1)
        self.game.incrementScore(self.p1)
        self.assertTrue(self.game.isFinished())
        self.assertRaises(GameAlreadyFinishedError, self.game.incrementScore, self.p2)
        
    def test_incrementScore_wrongPlayer(self):
        p3 = Player("name3","surname3",None,1)
        self.assertRaises(InvalidPlayerError, self.game.incrementScore, p3)
        
if __name__ == "__main__":
    unittest.main()