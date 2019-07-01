# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod


class Camera(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def shoot(self):
        pass
