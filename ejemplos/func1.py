from dataclasses import dataclass
import numpy as np
import xarray as xr
#from enum import Enum
from typing import Union

number_type = Union[float, int, np.float_, np.int_]

@dataclass
class Struct2D:
    points: xr.DataArray
    bars: xr.DataArray

    @property
    def points(self):
        return self.points_

    def __init__(self):
        self.points_ = xr.DataArray([[]], dims=["x", "y"], coords=None)
        self.bars_ = xr.DataArray([[]], dims=["N", "F"], coords=None)
    
    def add_point(self, x: number_type, y: number_type):
        if not isinstance(x, number_type):
            raise TypeError(f"x={x} is not of any admisible type.")
        if not isinstance(y, number_type):
            raise TypeError(f"y={y} is not of any admisible type.")

        self.points_[(x=)]
