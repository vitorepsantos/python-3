# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod


class FilterWheel(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def rotate(self, posix: int):
        pass
