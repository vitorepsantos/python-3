# -*- coding: utf-8 -*-
from .filter_wheel import FilterWheel


class FilterWheelDefault(FilterWheel):

    def __init__(self):
        super().__init__()

    def rotate(self, posix: int):
        print("Rotate to posix: " + str(posix))
