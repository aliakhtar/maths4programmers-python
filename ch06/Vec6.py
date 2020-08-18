from ch06.CoordinateVector import CoordinateVector


class Vec6(CoordinateVector):

    @classmethod
    def zero(cls):
        return Vec6(0, 0, 0, 0, 0, 0)

    def dimension(self):
        return 6
