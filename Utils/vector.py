from math import sqrt


class Vector3:
    def __init__(self, x=1.0, y=1.0, z=1.0):
        self._x = x
        self._y = y
        self._z = z

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def z(self):
        return self._z

    def __add__(self, other):
        if isinstance(other, Vector3):
            return self._x + other.x, self._y + other.y, self._z + other.x
        raise TypeError(f'Cannot add a Vector3 with a {type(other)}')

    def __sub__(self, other):
        if isinstance(other, Vector3):
            return self._x - other.x, self._y - other.y, self._z - other.x
        raise TypeError(f'Cannot subtract a Vector3 with a {type(other)}')

    def __mul__(self, other):
        if isinstance(other, Vector3):
            return self._x * other.x, self._y * other.y, self._z * other.x
        if isinstance(other, float) or isinstance(other, int):
            return self._x * other, self._y * other, self._z * other
        raise TypeError(f'Cannot multiply a Vector3 with a {type(other)}')

    def __truediv__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return self._x / other, self._y / other, self._z / other
        raise TypeError(f'Cannot divide a Vector3 with a {type(other)}')

    def length(self):
        return sqrt(self._x * self._x + self._y * self._y + self._z * self._z)

    def squared_length(self):
        return self._x * self._x + self._y * self._y + self._z * self._z

    @staticmethod
    def dot(v1, v2):
        if not isinstance(v1, Vector3):
            raise TypeError(f'v1: expected Vector3, but got {type(v1)}')
        if not isinstance(v2, Vector3):
            raise TypeError(f'v2: expected Vector3, but got {type(v2)}')
        return v1.x * v2.x + v1.y * v2.y + v1.z * v2.z

    @staticmethod
    def cross(v1, v2):
        if not isinstance(v1, Vector3):
            raise TypeError(f'v1: expected Vector3, but got {type(v1)}')
        if not isinstance(v2, Vector3):
            raise TypeError(f'v2: expected Vector3, but got {type(v2)}')
        return Vector3(v1.y * v2.z - v1.z * v2.y,
                       v1.z * v2.x - v1.x * v2.z,
                       v1.x * v2.y - v1.y * v2.x)

    @staticmethod
    def unit(v):
        if not isinstance(v, Vector3):
            raise TypeError(f'{type(v)} is not a Vector3')
        return v / v.length()

    def __str__(self):
        return f"[{self._x}, {self._y}, {self._z}]"
