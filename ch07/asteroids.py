import pygame
from math import pi, sqrt, cos, sin, atan2
from random import uniform, randint
from ch07.vectors import *


class PolygonModel():
    def __init__(self, points):
        self.points = points
        self.angle = 0
        self.x = 0
        self.y = 0

    def transformed(self):
        return (self.x, self.y)


class Ship(PolygonModel):
    def __init__(self):
        super().__init__([(0.5, 0), (-0.25, 0.25), (-0.25, -0.25)])


class Asteroid(PolygonModel):
    def __init__(self):
        sides = randint(5, 9)
        vectors = [to_cartesian((uniform(0.5, 10), 2 * pi * i / sides))
                   for i in range(sides)]

        super().__init__(vectors)
