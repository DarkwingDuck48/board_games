"""
Классы шахматных фигур
1. Знать что за фигура (иконка, цвет)
2. Как ходит фигура (уметь вычислить доступные перемещения)

"""
from enum import Enum
from chess_exceptions import NotValidPieceName
from coordinates import Coordinate


class ColorPiece(Enum):
    BLACK = "BLACK"
    WHITE = "WHITE"


class Piece:
    icons: dict[ColorPiece, str] = {
        ColorPiece.WHITE: "",
        ColorPiece.BLACK: "",
        }

    def __init__(self, color: ColorPiece):
        self.color = color
        self.position = None
        self.icon = self.icons[color]

    def __str__(self) -> str:
        return self.icon


class King(Piece):
    icons: dict[ColorPiece, str] = {
        ColorPiece.WHITE: "\u2654",
        ColorPiece.BLACK: "\u265A",
        }

    def possible_moves(self, start_position: Coordinate) -> list[Coordinate]:
        valid_file_offset = list(range(-1, 2))
        valid_rank_offset = list(range(-1, 2))
        for file_move in valid_file_offset:
            for rank_move in valid_rank_offset:
                print(f"Move: {files[start_position[0] + file_move]}{start_position[1] + rank_move}")


class Queen(Piece):
    icons: dict[ColorPiece, str] = {
        ColorPiece.WHITE: "\u2655",
        ColorPiece.BLACK: "\u265B",
        }


class Rook(Piece):
    icons: dict[ColorPiece, str] = {
        ColorPiece.WHITE: "\u2656",
        ColorPiece.BLACK: "\u265C",
        }


class Bishop(Piece):
    icons: dict[ColorPiece, str] = {
        ColorPiece.WHITE: "\u2657",
        ColorPiece.BLACK: "\u265D",
        }


class Knight(Piece):
    icons: dict[ColorPiece, str] = {
        ColorPiece.WHITE: "\u2658",
        ColorPiece.BLACK: "\u265E",
        }


class Pawn(Piece):
    icons: dict[ColorPiece, str] = {
        ColorPiece.WHITE: "\u2659",
        ColorPiece.BLACK: "\u265F",
        }


class PieceFactory:
    def __init__(self):
        self.pieces = {
            "r": Rook(ColorPiece.BLACK),
            "n": Knight(ColorPiece.BLACK),
            "b": Bishop(ColorPiece.BLACK),
            "q": Queen(ColorPiece.BLACK),
            "k": King(ColorPiece.BLACK),
            "p": Pawn(ColorPiece.BLACK),
            "R": Rook(ColorPiece.WHITE),
            "N": Knight(ColorPiece.WHITE),
            "B": Bishop(ColorPiece.WHITE),
            "Q": Queen(ColorPiece.WHITE),
            "K": King(ColorPiece.WHITE),
            "P": Pawn(ColorPiece.WHITE),
            }

    def get_piece(self, str_notation: str) -> Piece:
        if self.pieces.get(str_notation, None) is None:
            raise NotValidPieceName(f"{str_notation} is unknown piece")
        return self.pieces[str_notation]
