# -*- coding: utf-8 -*-
from .camera import Camera


class CameraCanon(Camera):

    def __init__(self):
        super().__init__()

    def shoot(self):
        print("Shoot from Canon")
