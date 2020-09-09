import pygame
from math import pi, sqrt, cos, sin, atan2, fabs
from random import uniform, randint
from ch11.vectors import *
from ch11.asteroids import *

ship = Ship()
black_hole = BlackHole(0.1)
asteroids = [Asteroid() for _ in range(10)]

for a in asteroids:
    a.x = randint(-10, 10)
    a.y = randint(-10, 10)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
LIGHT_GRAY = (240, 240, 240)
DARK_GRAY = (128, 128, 128)

width, height = 400, 400
thrust = 3


def to_pixels(x, y):
    return (width / 2 + width * x / 20, height / 2 - height * y / 20)


def draw_poly(screen, polygon_model, color=BLACK, fill=False):
    pixel_points = [to_pixels(x, y) for x, y in polygon_model.transformed()]
    if fill:
        pygame.draw.polygon(screen, color, pixel_points, 0)
    else:
        pygame.draw.lines(screen, color, True, pixel_points, 2)
    if polygon_model.draw_center:
        cx, cy = to_pixels(polygon_model.x, polygon_model.y)
        pygame.draw.circle(screen, BLACK, (int(cx), int(cy)), 4, 4)


def draw_segment(screen, v1, v2, color=RED):
    pygame.draw.line(screen, color, to_pixels(*v1), to_pixels(*v2), 2)


def draw_grid(screen):
    for x in range(-9, 10):
        draw_segment(screen, (x, -10), (x, 10), color=LIGHT_GRAY)
    for y in range(-9, 10):
        draw_segment(screen, (-10, y), (10, y), color=LIGHT_GRAY)

    draw_segment(screen, (-10, 0), (10, 0), color=DARK_GRAY)
    draw_segment(screen, (0, -10), (0, 10), color=DARK_GRAY)


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

        for a in asteroids:
            a.move(milliseconds, (0, 0), black_hole)

        thrust_vector = (0, 0)
        if keys[pygame.K_LEFT]:
            ship.angle += milliseconds * (2 * pi / 1000)

        if keys[pygame.K_RIGHT]:
            ship.angle -= milliseconds * (2 * pi / 1000)

        if keys[pygame.K_UP]:
            thrust_vector = to_cartesian((thrust_vector, ship.angle))
        elif keys[pygame.K_DOWN]:
            thrust_vector = to_cartesian((-thrust, ship.angle))

        ship.move(milliseconds, thrust_vector, black_hole)

        laser = ship.laser_segment()

        # screen.fill(BLACK)
        screen.fill(WHITE)

        if keys[pygame.K_SPACE]:
            draw_segment(screen, *laser, color=RED)

        draw_poly(screen, ship)
        draw_poly(screen, black_hole, fill=True)

        for a in asteroids:
            if keys[pygame.K_SPACE] and a.does_intersect(laser):
                asteroids.remove(a)
            else:
                draw_poly(screen, a, color=GREEN)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
