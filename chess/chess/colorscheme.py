"""
Раскраска сообщения в терминале
"""

from enum import Enum


class ColorsEnum(Enum):
    BLACK = "\u001B[30m"
    WHITE = "\u001B[37m"
    RED = "\u001B[31m"
    GREEN = "\u001B[32m"
    BLUE = "\u001B[34m"
    YELLOW = "\u001B[33m"
    PURPLE = "\u001B[35m"
    CYAN = "\u001B[36m"


class ColorsBackground(Enum):
    BLACK = "\u001B[40m"
    WHITE = "\u001B[47m"
    RED = "\u001B[41m"
    GREEN = "\u001B[42m"
    BLUE = "\u001B[44m"
    YELLOW = "\u001B[43m"
    PURPLE = "\u001B[45m"
    CYAN = "\u001B[46m"


class ColorScheme:
    def __init__(
            self, color: ColorsEnum | None = None, bgr: ColorsBackground | None = None
            ):
        self.ANSI_RESET = "\u001B[0m"
        self.color = color.value if color else ""
        self.background = bgr.value if bgr else ""

    def colorise(self, value: str) -> str:
        return f"{self.color}{self.background}{value}{self.ANSI_RESET}"
