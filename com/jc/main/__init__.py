"""
Main Module

@author: Javi Carretero
"""
from com.jc.match import Match
from com.jc import CHAMPIONSHIP_MATCH
from com.jc.player import Player

def main():
    # List of players
    nadal = Player("Rafael","Nadal","Rafa Nadal",4)
    djokovic = Player("Novak","Djokovic","Djokovic",1)
    
    m = Match(CHAMPIONSHIP_MATCH)
    m.addPlayers(nadal)
    m.addPlayers(djokovic)
    
    m.startMatch()
    
if __name__ == "__main__":
    main()