from enums import Player
from Piece import King, Queen, Pawn, Rook, Bishop, Knight

class game_state:
    def __init__(self):
        self.current_player = Player.PLAYER_1  # מתחילים בלבן
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.white_king_pos = (7, 4)
        self.black_king_pos = (0, 4)
        self.check = False
        self.checkmate = False
        self.turn = Player.PLAYER_1

    def move_piece(self, start, end, is_ai=False):
        piece = self.board[start[0]][start[1]]
        self.board[end[0]][end[1]] = piece
        self.board[start[0]][start[1]] = None
        piece.set_position(end[0], end[1])

        # עדכון מיקום המלך אם צריך
        if piece.get_name() == "k":
            if piece.get_player() == Player.PLAYER_1:
                self.white_king_pos = (end[0], end[1])
            else:
                self.black_king_pos = (end[0], end[1])

        # קביעת השחקן שמתקיף (המי שזז) והיריב
        attacker = piece.get_player()
        opponent = Player.PLAYER_2 if attacker == Player.PLAYER_1 else Player.PLAYER_1

        # בדיקת check ו־checkmate על היריב
        self.check = self.in_check(opponent)
        self.checkmate = self.is_checkmate(opponent)

        # החלפת תור
        self.current_player = opponent

    def in_check(self, player):
        # בינתיים נשתמש באותה פונקציה לגילוי check
        return self._is_attacked(player)

    def is_checkmate(self, player):
        # פונקציה לבדיקת checkmate, כרגע זהה לבדיקת התקפה
        return self._is_attacked(player)

    def _is_attacked(self, player):
        # בדיקת האם המלך של player מותקף על ידי מלכה של היריב
        king_pos = self.white_king_pos if player == Player.PLAYER_1 else self.black_king_pos
        for row in self.board:
            for piece in row:
                if piece and piece.get_player() != player and piece.get_name() == "q":
                    pr, pc = piece.get_position()
                    # בדיקת תקיפה לאלכסון, שורה או עמודה
                    if (abs(pr - king_pos[0]) == abs(pc - king_pos[1]) or
                        pr == king_pos[0] or pc == king_pos[1]):
                        return True
        return False
