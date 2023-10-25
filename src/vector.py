import math

class Vector:
    def __init__(values):
        if isinstance(values, list):
            self.values = values
        else:
            raise ValueError("Use lists.")

    @property
    def size(self):
        return len(self.values)

    def __len__(self):
        return len(self.values)

    @property
    def dtype(self):
        return type(self.values[0])

    # Vector operations
    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must have the same length for addition")
        return Vector([x + y for x, y in zip(self.values, other.values)])

    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must have the same length for subtraction")
        return Vector([x - y for x, y in zip(self.values, other.values)])

    def __mul__(self, other):
        if hasattr(other, "__iter__"):
            assert len(self) == len(other)
            return Vector([x * y for x, y in zip(self.values, other)])
        return Vector([x * scalar for x in self.values])

    def dot(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must have the same length for dot product")
        return sum(x * y for x, y in zip(self.values, other.values))

    def __getitem__(self, i):
        try:
            return self.values[i]
        except Exception:
            raise IndexError("TODO!")

    def __setitem__(self, i, value):
        if not isinstance(value, self.dtype): raise ValueError(f"new value must be of {self.dtype} type.")
        self.values[i] = value

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.values):
            result = self.values[self.index]
            self.index += 1
            return result
        raise StopIteration