#! /usr/bin/env python3
from src.core.camera.camera_enum import CameraEnum
from src.core.camera.camera_factory import CameraFactory
from src.core.imager import Imager
from src.core.imager_factory import ImagerFactory
from src.core.shutter.shutter_enum import ShutterEnum
from src.core.shutter.shutter_factory import ShutterFactory

_camera_factory: CameraFactory = CameraFactory()
_shutter_factory: ShutterFactory = ShutterFactory()

_imager_factory: ImagerFactory = ImagerFactory(_camera_factory, _shutter_factory)
_imager: Imager = _imager_factory.factory(CameraEnum.SONY, ShutterEnum.DIAPHRAGM)

_imager.open_shutter()
_imager.shoot()
_imager.close_shutter()