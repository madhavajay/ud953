# -*- coding: utf-8 -*-
# Author: github.com/madhavajay
"""This is a utility class for testing almost zero"""

from decimal import Decimal


class InaccurateDecimal(Decimal):
    """Utility wrapper class to detect values close to 0"""
    def is_near_zero(self, eps=1e-10):
        """Checks if value is virtually 0"""
        return abs(self) < eps
