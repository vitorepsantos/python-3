from abc import ABC, abstractmethod


class Shutter(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def close(self):
        pass