
from Piece import Knight

class AllEnemiesGameState:
    def get_piece(self, row, col):
        class Enemy:
            def get_player(self): return 'b'
        return Enemy()
    def is_valid_piece(self, row, col): return True

class NoEnemiesGameState:
    def get_piece(self, row, col):
        return None
    def is_valid_piece(self, row, col): return False

class SingleEnemyGameState:
    def get_piece(self, row, col):
        class Enemy:
            def get_player(self): return 'b'
        if (row, col) == (5, 6): return Enemy()
        return None
    def is_valid_piece(self, row, col):
        return (row, col) == (5, 6)

def test_knight_all_takes():
    knight = Knight('n', 4, 4, 'w')
    gs = AllEnemiesGameState()
    expected = [(2, 3), (2, 5), (3, 2), (3, 6),
                (5, 2), (5, 6), (6, 3), (6, 5)]
    actual = knight.get_valid_piece_takes(gs)
    assert sorted(actual) == sorted(expected)

def test_knight_no_takes():
    knight = Knight('n', 3, 3, 'w')
    gs = NoEnemiesGameState()
    expected = []
    actual = knight.get_valid_piece_takes(gs)
    assert actual == expected

def test_knight_single_take():
    knight = Knight('n', 4, 4, 'w')
    gs = SingleEnemyGameState()
    expected = [(5, 6)]
    actual = knight.get_valid_piece_takes(gs)
    assert actual == expected
