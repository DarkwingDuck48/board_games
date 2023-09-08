"""
Класс координат
rank - горизонталь
files - вертикаль

Так как мы знаем, что доска у нас 8х8, то можем сразу определить валидность перемещения

"""
from chess_exceptions import NotValidCoordinate


class Coordinate:
    files: dict[str, int] = {
        "a": 0,
        "b": 1,
        "c": 2,
        "d": 3,
        "e": 4,
        "f": 5,
        "g": 6,
        "h": 7
        }

    def __init__(self, file: str | int, rank: int, piece=None) -> None:
        """
        :param file: Вертикаль доски
        :param rank: Горизонталь доски
        :param piece: Фигура на координате
        """
        if not self._is_valid_coordinate(file, rank):
            raise NotValidCoordinate(f"Выбрана неверная ячейка {file}{rank}")
        self.file, self.file_letter = self._convert_file(file)
        self.rank = rank - 1
        self.piece = piece

    def _convert_file(self, file: str | int) -> tuple[int, str]:
        try:
            file = int(file) - 1  # вычитаем 1, потому что индексы начинаются с 0
            letter = list(self.files.keys())[file]
            return file, letter
        except ValueError:
            return self.files[file.lower()], file

    def _is_valid_coordinate(self, file: str | int, rank: int) -> bool:
        try:
            file = int(file)
            return len(self.files) >= file and rank in range(1, 9)
        except ValueError:
            return self.files.get(file.lower(), None) is not None and rank in range(1, 9)

    def __eq__(self, other):
        return self.file == other.file and self.rank == other.rank

    def __str__(self):
        return f"{self.file_letter.lower()}{self.rank + 1}"

    def set_piece(self, piece):
        self.piece = piece

    def delete_piece(self):
        self.piece = None


if __name__ == "__main__":
    print(Coordinate("a", 2))
