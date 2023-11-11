from dataclasses import dataclass
import numpy as np
import xarray as xr
#from enum import Enum
from typing import Union

number_type = Union[float, int, np.float_, np.int_]
int_type = Union[int, np.int_]

@dataclass
class Struct2D:
    points: xr.DataArray
    bars: xr.DataArray

    @property
    def points(self):
        return self.points_

    def __init__(self):
        self.points_ = xr.DataArray([[]], dims=["Pos.", "n"], coords={"Pos.": ["x", "y"]})
        self.points_ = np.float_
        self.bars_ = xr.DataArray([[]], dims=["Points", "n"], coords={"Points": ["N", "F"]})
        self.bars_.dtype = np.int_
    
    def add_point(self, x: number_type, y: number_type):
        if not isinstance(x, number_type):
            raise TypeError(f"x={x} is not of any admisible type.")
        if not isinstance(y, number_type):
            raise TypeError(f"y={y} is not of any admisible type.")
        self.points_.loc[self.points_.shape[0]] = (x, y)

    def check_point(self, p: int_type):
        if p in self.points_['Pos']:
            return True
        return False

    def add_bar(self, N: int_type, F: int_type):
        assert check_point(N)
        assert check_point(F)


