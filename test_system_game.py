import pytest
from chess_engine import game_state
from enums import Player
from Piece import Queen, King, Pawn

def test_fools_mate():
    # יצירת לוח חדש
    gs = game_state()

    # איפוס לוח והצבת כלים מינימליים למט טיפשים
    gs.board = [[None for _ in range(8)] for _ in range(8)]

    # הצבת מלכים
    gs.board[0][4] = King("k", 0, 4, Player.PLAYER_2)  # שחור
    gs.board[7][4] = King("k", 7, 4, Player.PLAYER_1)  # לבן

    # הצבת מלכה שחורה
    gs.board[0][3] = Queen("q", 0, 3, Player.PLAYER_2)

    # הצבת רגלים לבנים שמאפשרים את המט
    gs.board[6][5] = Pawn("p", 6, 5, Player.PLAYER_1)
    gs.board[6][6] = Pawn("p", 6, 6, Player.PLAYER_1)

    # מהלך 1: לבן - רגלי ל־f3
    gs.move_piece((6, 5), (5, 5), is_ai=False)

    # מהלך 2: שחור - כלום (מדלגים)

    # מהלך 3: לבן - רגלי ל־g4
    gs.move_piece((6, 6), (4, 6), is_ai=False)

    # מהלך 4: שחור - מלכה ל־h4 (מט)
    gs.move_piece((0, 3), (4, 7), is_ai=False)

    # בדיקה אם המשחק הסתיים
    assert gs.checkmate is True
