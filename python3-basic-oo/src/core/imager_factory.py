from src.core.camera.camera_enum import CameraEnum
from src.core.filterwheel.filter_wheel_factory import FilterWheelFactory
from src.core.shutter.shutter_enum import ShutterEnum
from src.core.shutter.shutter_factory import ShutterFactory
from .imager_default import ImagerDefault
from src.core.camera.camera_factory import CameraFactory


class ImagerFactory(object):

    def __init__(self, camera_factory: CameraFactory, shutter_factory: ShutterFactory
                 , filter_wheel_factory: FilterWheelFactory):
        self._camera_factory = camera_factory
        self._shutter_factory = shutter_factory
        self._filter_wheel_factory = filter_wheel_factory

    def factory(self, camera_type: CameraEnum, shutter_type: ShutterEnum):
        _camera = self._camera_factory.factory(camera_type)
        _shutter = self._shutter_factory.factory(shutter_type)
        _filter_wheel = self._filter_wheel_factory.factory()
        _imager_default = ImagerDefault(_camera, _shutter, _filter_wheel)
        return _imager_default
