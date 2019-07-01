# -*- coding: utf-8 -*-
from .shutter_diaphragm import ShutterDiaphragm
from .shutter_board import ShutterBoard
from .shutter_enum import ShutterEnum


class ShutterFactory(object):

    def factory(self, shutter_type: ShutterEnum):
        if shutter_type == ShutterEnum.DIAPHRAGM:
            return ShutterDiaphragm()
        if shutter_type == ShutterEnum.BOARD:
            return ShutterBoard()
