# -*- coding: utf-8 -*-
# Author: github.com/madhavajay
"""This is a custom error class for non zero elements"""


class NoNonZeroElements(Exception):
    """Custom Error for No Non Zero Elements in a Plane"""
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)
