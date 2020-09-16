import pygame, pygame.sndarray
import numpy as np

pygame.mixer.init(frequency=44100, size=-16, channels=1)
arr = np.random.randint(-32768, 32767, size=44100, dtype="int16")
sound = pygame.sndarray.make_sound(arr)
sound.play()