class ChessGame():
    def __init__(self, player):
        self.player = player

    def make_move(self):
        return f"{self.player} make a move!"

chino = ChessGame("Chino") 

chino.make_move()