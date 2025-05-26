import logging
from chess_engine import game_state
from ai_engine import chess_ai
from enums import Player

logging.basicConfig(
    filename='chess_log.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def simulate_game():
    gs = game_state()
    ai = chess_ai()
    knight_moves_count = 0
    move_number = 1

    while True:
        player = Player.PLAYER_1 if gs.whose_turn() else Player.PLAYER_2

        all_moves = gs.get_all_legal_moves(player)
        if not all_moves:
            logging.info("No valid moves remaining. Exiting.")
            break

        # Decide move
        if player == Player.PLAYER_1:
            move = ai.minimax_black(gs, 3, -100000, 100000, True, player)
        else:
            move = ai.minimax_white(gs, 3, -100000, 100000, True, player)

        from_sq, to_sq = move
        piece = gs.get_piece(from_sq[0], from_sq[1])

        if piece.get_name() == 'n':
            knight_moves_count += 1
            logging.debug(f"Knight moved from {from_sq} to {to_sq}")

        logging.info(f"Move {move_number}: {piece.get_name()} from {from_sq} to {to_sq}")
        move_number += 1

        gs.move_piece(from_sq, to_sq, True)

        result = gs.checkmate_stalemate_checker()
        if result == 0:
            logging.info("Game Over: Black wins")
            break
        elif result == 1:
            logging.info("Game Over: White wins")
            break
        elif result == 2:
            logging.info("Game Over: Stalemate")
            break

    logging.info(f"Total knight moves: {knight_moves_count}")


if __name__ == "__main__":
    simulate_game()
