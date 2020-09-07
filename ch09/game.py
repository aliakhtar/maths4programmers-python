import pygame
from math import pi, sqrt, cos, sin, atan2, fabs
from random import uniform, randint
from ch09.vectors import *
from ch09.asteroids import *

ship = Ship()
asteroids = [Asteroid() for _ in range(10)]

for a in asteroids:
    a.x = randint(-10, 10)
    a.y = randint(-10, 10)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

width, height = 400, 400


def to_pixels(x, y):
    # new_x = (x + 10) * 20
    # new_y = fabs((y - 10) * 20)
    # return (new_x, new_y)
    return (width / 2 + width * x / 20, height / 2 - height * y / 20)


def draw_poly(screen, polygon_model, color=GREEN):
    pixel_points = [to_pixels(x, y) for x, y in polygon_model.transformed()]
    pygame.draw.aalines(screen, color, True, pixel_points, 10)


def draw_segment(screen, v1, v2, color=RED):
    pygame.draw.aaline(screen, color, to_pixels(*v1), to_pixels(*v2), 10)


def main():
    pygame.init()

    screen = pygame.display.set_mode([width, height])

    pygame.display.set_caption("Asteroids!")

    done = False
    clock = pygame.time.Clock()

    while not done:

        clock.tick()

        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop

        milliseconds = clock.get_time()
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            ship.angle += milliseconds * (2*pi / 1000)

        if keys[pygame.K_RIGHT]:
            ship.angle -= milliseconds * (2*pi / 1000)

        laser = ship.laser_segment()

        screen.fill(BLACK)

        if keys[pygame.K_SPACE]:
            draw_segment(screen, *laser, color=RED)

        draw_poly(screen, ship, color=WHITE)

        for a in asteroids:
            if keys[pygame.K_SPACE] and a.does_intersect(laser):
                asteroids.remove(a)
            else:
                draw_poly(screen, a, color=GREEN)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
