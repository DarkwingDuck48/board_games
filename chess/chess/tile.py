from typing import Optional

from colorscheme import ColorsEnum, ColorsBackground, ColorScheme
from piece import Piece


class Tile:
    """
        Объект одной клетки на поле.
        Можем сразу определеять цвет, так как знаем о нем все))
    """

    def __init__(self, file, rank, piece: Optional[Piece] = None) -> None:
        self.file = file
        self.rank = rank
        self.selected = False
        self.color = self._set_tile_color()
        self.selected_color = ColorScheme(ColorsEnum.GREEN, ColorsBackground.GREEN)
        self.piece = piece

    def _set_tile_color(self):
        if (self.file + self.rank) % 2 == 0:
            return ColorScheme(ColorsEnum.WHITE, ColorsBackground.WHITE)
        return ColorScheme(ColorsEnum.BLACK, ColorsBackground.BLACK)

    def __str__(self) -> str:
        display = self.piece if self.piece else " "
        if self.selected:
            return self.selected_color.colorise(f" {display} ")
        return self.color.colorise(f" {display} ")

    def __repr__(self) -> str:
        if self.piece is None:
            return f"({self.file}, {self.rank})"
        return str(self.piece)

    def is_empty(self) -> bool:
        return self.piece is None

    def put_piece(self, piece: Piece):
        self.piece = piece
