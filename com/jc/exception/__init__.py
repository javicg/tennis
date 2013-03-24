class PlayerNumberError(Exception):
    """Exception indicating the current number of players is wrong for a tennis match"""
    def __init__(self, numPlayers):
        self.currentPlayers = numPlayers
    
    def __str__(self):
        return "Number of players must be 2 (current number of players: " + str(self.currentPlayers) + ")"

class NoMorePlayersError(Exception):
    """Exception raised when trying to add more than 2 players to a tennis match"""
    def __str__(self):
        return "Number of players must not exceed 2 in a tennis match"
    
class MatchAlreadyStartedError(Exception):
    """Exception raised when a user wants to restart a Match"""
    def __str__(self):
        return "The Match has already been started"
    
class GameAlreadyFinishedError(Exception):
    """Exception raised when incrementing the score of a player in a closed Game"""
    def __str__(self):
        return "The score of a finished Game can't be modified"
    
class SetAlreadyFinishedError(Exception):
    """Exception raised when incrementing the score of a player in a closed Set"""
    def __str__(self):
        return "The score of a finished Set can't be modified"
    
class MatchAlreadyFinishedError(Exception):
    """Exception raised when incrementing the score of a player in a closed Match"""
    def __str__(self):
        return "The score of a finished Match can't be modified"
    
class InvalidPlayerError(Exception):
    """Exception raised when the player specified as a parameter is not a valid player in the match"""
    def __init__(self, player):
        self.player = player
        
    def __str__(self):
        return "Player " + str(self.player) + " is not a valid Player of the Match"