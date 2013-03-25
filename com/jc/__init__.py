CHAMPIONSHIP_MATCH = "Championship Match"
NORMAL_MATCH = "Normal Match"

class Point(object):
    """Parent class for all scoring types in Tennis"""
    def __init__(self):
        self._scorings = []
        self._winner = None
        
    def incrementScore(self, player):
        raise NotImplementedError("Unsupported method. No implementation found!")
    
    def score(self,player=None):
        raise NotImplementedError("Unsupported method. No implementation found!")
    
    def getActualPoint(self):
        if(len(self._scorings) == 0):
            return self # Empty scoring list = no subPoints considered
        return self._scorings[len(self._scorings) - 1]
    
    def getNumScoringsWon(self,player):
        return len(filter(lambda n: n.isFinished() and n.getWinner() == player, self._scorings))
    
    def getNumScoringsLost(self,player):
        return len(filter(lambda n: n.isFinished() and n.getWinner() != player, self._scorings))
    
    def getWinner(self):
        return self._winner
    
    def isFinished(self):
        return self._winner is not None
    
    def _newScoring(self):
        raise NotImplementedError("Unsupported method. No implementation found!")