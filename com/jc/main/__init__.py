"""
Main Module

@author: Javi Carretero
"""
from com.jc.match import Match
from com.jc import CHAMPIONSHIP_MATCH, NORMAL_MATCH
from com.jc.player import Player

def main():
    # List of players
    nadal = Player("Rafael","Nadal","Nadal",4)
    djokovic = Player("Novak","Djokovic","Djokovic",1)
    
    m = Match(NORMAL_MATCH)
    m.addPlayers(nadal)
    m.addPlayers(djokovic)
    
    m.startMatch()
    print m.score()
    
    m.incrementScore(nadal)
    m.incrementScore(nadal)
    m.incrementScore(nadal)
    m.incrementScore(nadal)
    
    m.incrementScore(djokovic)
    m.incrementScore(djokovic)
    m.incrementScore(djokovic)
    m.incrementScore(djokovic)
    
    m.incrementScore(nadal)
    m.incrementScore(nadal)
    m.incrementScore(nadal)
    m.incrementScore(nadal)
    
    m.incrementScore(djokovic)
    m.incrementScore(djokovic)
    m.incrementScore(djokovic)
    m.incrementScore(djokovic)
    
    m.incrementScore(nadal)
    m.incrementScore(nadal)
    m.incrementScore(nadal)
    m.incrementScore(nadal)
    
    m.incrementScore(djokovic)
    m.incrementScore(djokovic)
    m.incrementScore(djokovic)
    m.incrementScore(djokovic)
    
    m.incrementScore(nadal)
    m.incrementScore(nadal)
    m.incrementScore(nadal)
    m.incrementScore(nadal)
    
    m.incrementScore(djokovic)
    m.incrementScore(djokovic)
    m.incrementScore(djokovic)
    m.incrementScore(djokovic)
    
    m.incrementScore(nadal)
    m.incrementScore(nadal)
    m.incrementScore(nadal)
    m.incrementScore(nadal)
    
    m.incrementScore(djokovic)
    m.incrementScore(djokovic)
    m.incrementScore(djokovic)
    m.incrementScore(djokovic)
    
    m.incrementScore(nadal)
    m.incrementScore(nadal)
    m.incrementScore(nadal)
    m.incrementScore(nadal)
    
    m.incrementScore(djokovic)
    m.incrementScore(djokovic)
    m.incrementScore(djokovic)
    m.incrementScore(djokovic)
    
    m.incrementScore(nadal)
    m.incrementScore(nadal)
    m.incrementScore(nadal)
    m.incrementScore(nadal)
    m.incrementScore(nadal)
    m.incrementScore(nadal)
    m.incrementScore(nadal)
    
    m.incrementScore(nadal)
    m.incrementScore(nadal)
    m.incrementScore(nadal)
    m.incrementScore(nadal)
    
    m.incrementScore(djokovic)
    m.incrementScore(djokovic)
    m.incrementScore(djokovic)
    m.incrementScore(djokovic)
    
    m.incrementScore(nadal)
    m.incrementScore(nadal)
    m.incrementScore(nadal)
    m.incrementScore(nadal)
    
    m.incrementScore(djokovic)
    m.incrementScore(djokovic)
    m.incrementScore(djokovic)
    m.incrementScore(djokovic)
    
    m.incrementScore(nadal)
    m.incrementScore(nadal)
    m.incrementScore(nadal)
    m.incrementScore(nadal)
    
    m.incrementScore(djokovic)
    m.incrementScore(djokovic)
    m.incrementScore(djokovic)
    m.incrementScore(djokovic)
    
    m.incrementScore(nadal)
    m.incrementScore(nadal)
    m.incrementScore(nadal)
    m.incrementScore(nadal)
    
    m.incrementScore(djokovic)
    m.incrementScore(djokovic)
    m.incrementScore(djokovic)
    m.incrementScore(djokovic)
    
    m.incrementScore(nadal)
    m.incrementScore(nadal)
    m.incrementScore(nadal)
    m.incrementScore(nadal)
    
    m.incrementScore(djokovic)
    m.incrementScore(djokovic)
    m.incrementScore(djokovic)
    m.incrementScore(djokovic)
    
    m.incrementScore(nadal)
    m.incrementScore(nadal)
    m.incrementScore(nadal)
    m.incrementScore(nadal)
    
    m.incrementScore(djokovic)
    m.incrementScore(djokovic)
    m.incrementScore(djokovic)
    m.incrementScore(djokovic)
    
    m.incrementScore(nadal)
    m.incrementScore(nadal)
    m.incrementScore(nadal)
    m.incrementScore(nadal)
    m.incrementScore(nadal)
    m.incrementScore(nadal)
    m.incrementScore(nadal)
    
    print m.score()
    
if __name__ == "__main__":
    main()