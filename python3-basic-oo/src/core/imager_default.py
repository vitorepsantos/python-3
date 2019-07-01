# -*- coding: utf-8 -*-
from src.core.camera.camera import Camera
from src.core.shutter.shutter import Shutter
from .imager import Imager


class ImagerDefault(Imager):

    def __init__(self, camera: Camera, shutter: Shutter):
        super().__init__()
        self._camera = camera
        self._shutter = shutter

    def shoot(self):
        self._camera.shoot()

    def open_shutter(self):
        self._shutter.open()

    def close_shutter(self):
        self._shutter.close()
