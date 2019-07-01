# -*- coding: utf-8 -*-
from .shutter import Shutter


class ShutterBoard(Shutter):

    def __init__(self):
        super().__init__()

    def open(self):
        print("Open ShutterBoard")

    def close(self):
        print("Close ShutterBoard")
