# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod


class Imager(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def shoot(self):
        pass

    @abstractmethod
    def open_shutter(self):
        pass

    @abstractmethod
    def close_shutter(self):
        pass

    @abstractmethod
    def rotate(self, posix: int):
        pass