# -*- coding: utf-8 -*-
from .camera_canon import CameraCanon
from .camera_sony import CameraSony
from .camera_enum import CameraEnum


class CameraFactory(object):

    def factory(self, camera_type: CameraEnum):
        if camera_type == CameraEnum.CANON:
            return CameraCanon()
        if camera_type == CameraEnum.SONY:
            return CameraSony()
