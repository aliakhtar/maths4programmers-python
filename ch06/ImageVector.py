from ch06.Vector import Vector
from PIL import Image


class ImageVector(Vector):
    size = (500, 500)

    def __init__(self, arg):
        try:
            img = Image.open(arg).resize(ImageVector.size)
            self.pixels = img.getdata()

        except:
            self.pixels = arg

    def img(self):
        img = Image.new('RGB', ImageVector.size)
        img.putdata([(int(r), int(g), int(b)) for r, g, b in self.pixels])
        return img

    def add(self, other):
        new_pixels = [(r1 + r2, g1 + g2, b1 + b2)
                      for ((r1, g1, b1), (r2, g2, b2)) in zip(self.pixels, other.pixels)]
        return ImageVector(new_pixels)

    def scale(self, s):
        new_pixels = [(r * s, g * s, b * s) for (r,g, b) in self.pixels]
        return ImageVector(new_pixels)

    # noinspection PyProtectedMember
    def _repr_png_(self):
        return self.img()._repr_png_()

    @classmethod
    def zero(cls):
        total_pixels = cls.size[0] * cls.size[1]
        zeroes = [(0, 0, 0) for _ in range(total_pixels)]
        return ImageVector(zeroes)
