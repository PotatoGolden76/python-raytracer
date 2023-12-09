from Utils.color import Color


class Image:
    def __init__(self, name="untitled.ppm", height=1, width=1):
        self._name = name
        self._height = height
        self._width = width

        self._data = [[Color(0, 0, 0) for _ in range(self._width)] for _ in range(self._height)]

    @property
    def name(self):
        return self._name

    @property
    def height(self):
        return self._height

    @property
    def width(self):
        return self._width

    def set_pixel_tuple(self, x, y, value):
        self._data[y][x] = Color.from_tuple(value)

    def set_pixel(self, x, y, color):
        self._data[y][x] = color

    def get_file_data(self):
        s = f"P3\n{self._width} {self._height}\n255\n"
        for line in self._data:
            for pixel in line:
                s += f"{pixel.red} {pixel.green} {pixel.blue}\t"
            s += "\n"

        return s
