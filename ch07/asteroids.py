import pygame
from math import pi, sqrt, cos, sin, atan2
from random import uniform, randint
from ch07.vectors import *
from ch07.functions import *


class PolygonModel():
    def __init__(self, points):
        self.points = points
        self.angle = 0
        self.x = 0
        self.y = 0

    def transformed(self):
        translation = (self.x, self.y)
        # rotated = self
        return translate(translation, [rotate2d(self.angle, p) for p in self.points])

    def segments(self):
        point_count = len(self.points)
        points = self.transformed()
        return [(points[i], points[(i + 1) % point_count])
                for i in range(0, point_count)]

    def does_intersect(self, other_segment):
        for segment in self.segments():
            if do_segments_intersect(other_segment, segment):
                return True

        return False


class Ship(PolygonModel):
    def __init__(self):
        super().__init__([(0.5, 0), (-0.25, 0.25), (-0.25, -0.25)])

    def laser_segment(self):
        dist = 20.0 * sqrt(2)  # No idea what this is doing but apparently its to find the longest point somehow?
        start_x, start_y = self.transformed()[0]
        end_x = dist * cos(self.angle)
        end_y = dist * sin(self.angle)
        return (
            (start_x, start_y),
            (end_x, end_y)
        )


class Asteroid(PolygonModel):
    def __init__(self):
        sides = randint(5, 9)
        vectors = [to_cartesian((uniform(0.5, 1.0), 2 * pi * i / sides))
                   for i in range(sides)]

        super().__init__(vectors)
