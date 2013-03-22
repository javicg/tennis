"""
Main Module

@author: Javi Carretero
"""
from com.jc.Match import Match
from com.jc import CHAMPIONSHIP_MATCH
from com.jc.Player import Player

def main():
    # List of players
    nadal = Player("Rafael","Nadal","Rafa Nadal",4)
    djokovic = Player("Novak","Djokovic","Djokovic",1)
    
    m = Match(CHAMPIONSHIP_MATCH)
    m.addPlayer(nadal)
    m.addPlayer(djokovic)
    
    m.startMatch()
    
if __name__ == "__main__":
    main()