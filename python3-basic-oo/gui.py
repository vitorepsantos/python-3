#! /usr/bin/env python3
import threading

from src.core.camera.camera_enum import CameraEnum
from src.core.camera.camera_factory import CameraFactory
from src.core.filterwheel.filter_wheel_factory import FilterWheelFactory
from src.core.imager import Imager
from src.core.imager_factory import ImagerFactory
from src.core.shutter.shutter_enum import ShutterEnum
from src.core.shutter.shutter_factory import ShutterFactory

_camera_factory: CameraFactory = CameraFactory()
_shutter_factory: ShutterFactory = ShutterFactory()
_filter_wheel_factory: FilterWheelFactory = FilterWheelFactory()
_imager_factory: ImagerFactory = ImagerFactory(_camera_factory, _shutter_factory, _filter_wheel_factory)


def threadable():
    _imager: Imager = _imager_factory.factory(CameraEnum.SONY, ShutterEnum.DIAPHRAGM)
    print(_imager.__hash__())


thread1 = threading.Thread(target=threadable)
thread2 = threading.Thread(target=threadable)
thread3 = threading.Thread(target=threadable)

thread1.start()
thread2.start()
thread3.start()
