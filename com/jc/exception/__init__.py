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