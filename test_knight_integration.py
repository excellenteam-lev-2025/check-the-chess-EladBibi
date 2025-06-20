from Piece import Knight
from enums import Player


class IntegrationGameState:
    def get_piece(self, row, col):
        # נגדיר רק אויבים בצד ימין של הפרש, כל שאר המשבצות ריקות
        enemy_positions = [(3, 2), (5, 6)]
        if (row, col) in enemy_positions:
            return Knight('n', row, col, Player.PLAYER_2)
        return None

    def is_valid_piece(self, row, col):
        return (0 <= row < 8) and (0 <= col < 8) and self.get_piece(row, col) is not None


def test_knight_get_valid_piece_moves_integration():
    knight = Knight('n', 4, 4, Player.PLAYER_1)
    gs = IntegrationGameState()
    expected_moves = [
        (2, 3), (2, 5),
        (3, 2),  # enemy
        (3, 6),
        (5, 2), (5, 6),  # enemy
        (6, 3), (6, 5)
    ]
    actual_moves = knight.get_valid_piece_moves(gs)
    assert sorted(actual_moves) == sorted(expected_moves)
