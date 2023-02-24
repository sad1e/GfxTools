# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 12:16:41 2023

@author: sad1e
"""

import math
import gfx_consts

def ior2specular(IOR: float):
    """
    Convert IOR to specular.
    """
    a = ( (IOR-1.0)/(IOR+1.0) )
    return a*a / gfx_consts.ReflectanceOfDielectric

def specular2ior(specular: float):
    """
    Convert specular to IOR.
    """
    return 1.0 / (2.0 / (math.sqrt(gfx_consts.ReflectanceOfDielectric * specular) + 1.0) - 1.0)

