from typing import Self

class SuperRapper:
    def __init__(self) -> None:
        self.__bpm = 120

    def tempo(self, bpm: int = 120) -> Self:
        self.__bpm = bpm
        return self

    def get_tempo(self) -> int:
        return self.__bpm
