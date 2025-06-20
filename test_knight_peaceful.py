from Piece import Knight

class EmptyGameState:
    def get_piece(self, row, col):
        return None

def test_knight_peaceful_moves_center():
    knight = Knight('n', 4, 4, 'w')
    gs = EmptyGameState()
    expected = [(2, 3), (2, 5),
                (3, 2), (3, 6),
                (5, 2), (5, 6),
                (6, 3), (6, 5)]
    actual = knight.get_valid_peaceful_moves(gs)
    assert sorted(actual) == sorted(expected)

def test_knight_peaceful_moves_corner():
    knight = Knight('n', 0, 0, 'w')
    gs = EmptyGameState()
    expected = [(1, 2), (2, 1)]
    actual = knight.get_valid_peaceful_moves(gs)
    assert sorted(actual) == sorted(expected)

class BlockedGameState:
    def get_piece(self, row, col):
        class Friendly:
            def get_player(self): return 'w'
        return Friendly()

def test_knight_peaceful_moves_blocked():
    knight = Knight('n', 4, 4, 'w')
    gs = BlockedGameState()
    expected = []
    actual = knight.get_valid_peaceful_moves(gs)
    assert actual == expected
