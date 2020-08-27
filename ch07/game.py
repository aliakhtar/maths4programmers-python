import pygame
from math import pi, sqrt, cos, sin, atan2, fabs
from random import uniform, randint
from ch07.vectors import *
from ch07.asteroids import *

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
    #new_x = (x + 10) * 20
    #new_y = fabs((y - 10) * 20)
    #return (new_x, new_y)
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
        screen.fill(BLACK)

        draw_poly(screen, ship, color=WHITE)
        draw_segment(screen, *ship.laser_segment(), color=RED)
        for a in asteroids:
            draw_poly(screen, a, color=GREEN)

        pygame.display.flip()

    pygame.quit()



if __name__ == "__main__":
    main()