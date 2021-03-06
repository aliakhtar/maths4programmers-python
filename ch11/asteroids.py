import pygame
from math import pi, sqrt, cos, sin, atan2
from random import uniform, randint
from ch11.vectors import *
from ch11.functions import *
from ch11.linear_solver import *

bounce = True
class PolygonModel():
    def __init__(self, points):
        self.points = points
        self.angle = 0
        self.x = 0
        self.y = 0
        self.vx = 0
        self.vy = 0
        self.draw_center = False

    def set_pos(self, v):
        x,y = v
        self.x = x
        self.y = y

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

    def does_collide(self, other_polygon):
        for segment in other_polygon.segments():
            if self.does_intersect(segment):
                return True

        return False

    def move(self, millis, thrust_vector, gravity_sources):
        secs = millis / 1000
        tx, ty = thrust_vector
        gx, gy = gravitational_field_sum(gravity_sources, self.x, self.y)
        ax = tx + gx
        ay = ty + gy

        self.vx += ax * secs
        self.vy += ay * secs

        self.x += self.vx * secs
        self.y += self.vy * secs

        if bounce:
            if self.x < -10 or self.x > 10:
                self.vx = - self.vx
            if self.y < -10 or self.y > 10:
                self.vy = - self.vy
        else:
            if self.x < -10:
                self.x += 20
            if self.y < -10:
                self.y += 20
            if self.x > 10:
                self.x -= 20
            if self.y > 10:
                self.y -=20


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
        self.vx = uniform(-1, 1)
        self.vy = uniform(-1, -1)


class BlackHole(PolygonModel):
    def __init__(self, gravity):
        vs = [to_cartesian((0.5, 2 * pi * i / 20)) for i in range(0, 20)]
        super().__init__(vs)
        self.gravity = gravity
