# -*- coding: utf-8 -*-
from src.core.camera.camera import Camera
from src.core.filterwheel.filter_wheel import FilterWheel
from src.core.shutter.shutter import Shutter
from .imager import Imager


class ImagerDefault(Imager):

    def __init__(self, camera: Camera, shutter: Shutter, filter_wheel: FilterWheel):
        super().__init__()
        self._camera = camera
        self._shutter = shutter
        self._filter_wheel = filter_wheel

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(ImagerDefault, cls).__new__(cls)
        return cls._instance

    def shoot(self):
        self._camera.shoot()

    def open_shutter(self):
        self._shutter.open()

    def close_shutter(self):
        self._shutter.close()

    def rotate(self, posix: int):
        self._filter_wheel.rotate(posix)
