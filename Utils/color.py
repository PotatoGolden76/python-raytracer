class Color:
    def __init__(self, red, green, blue):
        self._red = red
        self._green = green
        self._blue = blue

    @property
    def red(self):
        return self._red

    @property
    def green(self):
        return self._green

    @property
    def blue(self):
        return self._blue

    @staticmethod
    def from_tuple(tpl):
        return Color(tpl[0], tpl[1], tpl[2])

    def __str__(self):
        return f"(R: {self._red} G:{self._green} B:{self._blue})"
