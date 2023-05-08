import chess
import chess.engine
from stockfish import Stockfish
stockfish_location = "STOCKFISH_LOCATION"
engine = chess.engine.SimpleEngine.popen_uci(stockfish_location)
chessboard = chess.Board()

def get_best_move():
    '''Returns Best move acc to the board'''
    return engine.play(chessboard, chess.engine.Limit(time=0.1)).move