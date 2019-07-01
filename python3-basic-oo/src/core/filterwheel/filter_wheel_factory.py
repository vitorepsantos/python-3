# -*- coding: utf-8 -*-
from .filter_wheel_default import FilterWheelDefault


class FilterWheelFactory(object):

    def factory(self):
        return FilterWheelDefault()
