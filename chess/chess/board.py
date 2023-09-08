"""
Определение доски для игры
Поле для игры = 8х8

Первоначальная позиция на доске определяется по нотации FEN, дальше получаем по очереди ходы для белых и черных

"""
import sys

from typing import Optional
from string import ascii_lowercase

from tile import Tile
from colorscheme import ColorScheme, ColorsEnum, ColorsBackground
from piece import Piece, ColorPiece
from piece import King, Queen, Rook, Bishop, Knight, Pawn, PieceFactory
from coordinates import Coordinate
from chess_exceptions import NotValidCoordinateOffset, NotValidPieceName


class Board:
    def __init__(
            self, start_files: int, start_rank: int, start_position: Optional[str] = None
            ) -> None:
        """
        :param start_files: Количество стартовых вертикалей
        :param start_rank:  Количество стартовых горизонталей
        :param start_position: FEN нотация для стартовой позиции фигур
        """
        self.files = list(ascii_lowercase[:start_files])
        self.rank = tuple(range(start_rank, 0, -1))
        self.black_tile = ColorScheme(bgr = ColorsBackground.BLACK)
        self.white_tile = ColorScheme(bgr = ColorsBackground.WHITE)
        self.purple_tile = ColorScheme(ColorsEnum.PURPLE, ColorsBackground.PURPLE)
        self.board = []
        if start_position is None:
            start_position = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
        self._prepare_board(start_position)
        self.who_move = 'w'
        self.render()

    def _prepare_board(self, fen: Optional[str] = None):
        for rank_id in self.rank:
            row = []
            for file_id in range(len(self.files)):
                row.append(Tile(file_id, rank_id))
            self.board.append(row)
            # self.board.append([" "] * len(self.files))
        if fen is not None:
            self._parce_fen(fen)

    def _parce_fen(self, fen_notation: str):
        """
        Принимает на вход строку и парсит ее, расставляя фигуры в соответствии с нотацией
        rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1
        Описание доски идет сверху вниз.
        Где:
        rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR - состояние доски
        w или b - чей ход следующий
        KQkq - возможные рокировки kK - короткая рокировка (королевский фланг), Qq - длинная рокировка
        - возможность взять пешку на проходе (либо указывается поле, либо -)
        0 - счетчик полуходов, прошедших с последнего хода пешки или взятия фигуры
        1 - номер хода, увеличивается после хода черных на 1
        :return: Board
        """
        board_desc: list[str] = fen_notation.split(' ')
        rows_desc: list[str] = board_desc[0].split("/")
        factory = PieceFactory()
        for row_id, row in enumerate(rows_desc):
            current_file = 0
            current_rank = len(self.board) - row_id
            for letter in row:
                if letter.isnumeric():
                    current_file += int(letter)
                else:
                    piece = factory.get_piece(letter)
                    self.put_piece(piece, Coordinate(self.files[current_file], current_rank))
                    current_file += 1

    def get_tile_by_coordinate(self, coord: Coordinate) -> Piece | str:
        """Получаем информацию с доски по координате"""
        return self.board[coord.rank][coord.file]

    def move_piece(self, start_tile: Coordinate, end_tile: Coordinate):
        """
        Конечный результат = перемещению фигуры на новую позицию
        :param start_tile: Координата откуда перемещаем
        :param end_tile: Координата куда перемещаем
        :return:
        """
        self.board[end_tile.rank][end_tile.file] = self.board[start_tile.rank][start_tile.file]
        self.board[start_tile.rank][start_tile.file] = ' '
        self.render()

    def put_piece(self, piece: Piece, tile):
        # self.board[tile.rank][tile.file] = piece
        self.board[tile.rank][tile.file].put_piece(piece)

    def render(self, fen: Optional[str] = None):
        """Сумма индексов - нечетная = черный, четная - белый"""
        if fen is not None:
            self._parce_fen(fen)
        for rank_id in range(len(self.board), 0, -1):
            field = "".join(list(map(str, self.board[rank_id - 1]))) + f" {rank_id}"
            print(field)
        print("".join(list(f" {letter} " for letter in self.files)))


if __name__ == "__main__":
    board = Board(8, 8)
    # print(f"Make move: {Coordinate(5, 2)} -> {Coordinate('e', 4)}")
    # board.move_piece(Coordinate(5, 2), Coordinate("e", 4))
    # while True:
    #     start = input("Write start tile: ")
    #     if start == "q":
    #         sys.exit()
    #     start_coordinate = Coordinate(start[0], int(start[1]))
    #     end = input("Write end tile: ")
    #     if end == "q":
    #         sys.exit()
    #     end_coordinate = Coordinate(end[0], int(end[1]))
    #     board.move_piece(start_coordinate, end_coordinate)
