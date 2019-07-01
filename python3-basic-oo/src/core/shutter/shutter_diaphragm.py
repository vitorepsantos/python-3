# -*- coding: utf-8 -*-
from .shutter import Shutter


class ShutterDiaphragm(Shutter):

    def __init__(self):
        super().__init__()

    def open(self):
        print("Open ShutterDiaphragm")

    def close(self):
        print("Close ShutterDiaphragm")
