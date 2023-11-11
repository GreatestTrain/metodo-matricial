from dataclasses import dataclass
import numpy as np

from func import rot_2d, stiffness_2d

@dataclass
class Struct2D:
    points: np.ndarray
    supports: np.ndarray
    bars: np.ndarray[np.int]
    EAI: np.ndarray

    def __init__(self, n_points, n_bar):
        self.points_ = []
        self.bars_ = []

    @property
    def points(self):
        return np.array(self.points_)
    @points.set
    def points(self, points: list[np.ndarray] | np.ndarray):
        bar_points = np.unique(self.bars)
        for u in bar_points:
            if u not in list(range(len(points))):
                raise ValueError(f"A bar needs point: {u} defined.")
        self.points_ = None

    @property
    def bars(self):
        return np.array(self.bars_)

    def add_point(self, point: np.ndarray):
        point = np.array(point)
        if point.shape == (1, 2):
            point = np.squeeze(point)
        if point.shape != 2:
            raise ValueError()
        self.points_.append(point)

    def rm_point(self, idx: int = -1):
        bars = self.bars[~np.any( self.bars == idx, axis=1)]
        bars[bars > idx] -= 1
        self.bars_ = [*bars]
        self.points_.pop(idx)

    def add_bar(self, points: np.ndarray[np.int] | list[int]):
        if not isinstance(points, np.ndarray[np.int]) or not isinstance(points, list[int]):
            raise ValueError("Bar must contain two points.")
    
    @property
    def L(self):
        return np.linalg.norm(np.diff(self.points[self.bars], axis=1), axis=2)
    @property
    def alpha(self):
        return np.arctan(np.divide(*(np.diff(self.points[self.bars], axis=1).squeeze().T[::-1])))
    @property
    def At(self):
        return [rot_2d(alpha) for alpha in self.alpha]
        #return np.apply_along_axis(rot_2d, arr=self.alpha, axis=1)
    @property
    def Kl(self):
        return [stiffness_2d(E, A, I, L) for E, A, I, L in np.hstack(self.EAI, self.L)]
        #return np.apply_along_axis(stiffness_2d, arr=np.hstack([self.EAI, L]), axis=1)
    @property
    def Kt(self):
        return [A.T @ K @ A for A, K in zip(self.At, self.Kl)]
    @property
    def Gl(self):
        return self.supports[self.bars].reshape(-1, 6)
    @property
    def idx(self):
        return np.arange(0, self.supports.size)
    @property
    def Kg(self):
        _
        G_idx = _idx.reshape(len(S), -1)[B].reshape(-1, 6)
        for idx, K in zip(G_idx, Kt):
            zeros[*np.meshgrid(idx, idx)] += K
            


        