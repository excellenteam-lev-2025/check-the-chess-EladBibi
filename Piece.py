class Piece:
    def __init__(self, name, row, col, player):
        self.name = name
        self.row = row
        self.col = col
        self.player = player

    def get_position(self):
        return self.row, self.col

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def get_name(self):
        return self.name

    def get_player(self):
        return self.player

class King(Piece):
    pass

class Queen(Piece):
    pass

class Bishop(Piece):
    pass

class Rook(Piece):
    pass

class Pawn(Piece):
    pass

class Knight(Piece):
    def get_valid_peaceful_moves(self, gs):
        moves = []
        offsets = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
                   (1, -2), (1, 2), (2, -1), (2, 1)]
        for dr, dc in offsets:
            r, c = self.row + dr, self.col + dc
            if 0 <= r < 8 and 0 <= c < 8:
                if gs.get_piece(r, c) is None:
                    moves.append((r, c))
        return moves

    def get_valid_piece_takes(self, gs):
        moves = []
        offsets = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
                   (1, -2), (1, 2), (2, -1), (2, 1)]
        for dr, dc in offsets:
            r, c = self.row + dr, self.col + dc
            if 0 <= r < 8 and 0 <= c < 8:
                piece = gs.get_piece(r, c)
                # כאן אני תופס חלקי אויב בלבד
                if piece is not None and piece.get_player() != self.player:
                    if hasattr(gs, 'is_valid_piece') and gs.is_valid_piece(r, c):
                        moves.append((r, c))
        return moves

    def get_valid_piece_moves(self, gs):
        # איחוד תנועות ללא לקיחה ועם לקיחה
        return self.get_valid_peaceful_moves(gs) + self.get_valid_piece_takes(gs)
