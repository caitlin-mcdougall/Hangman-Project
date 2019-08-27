import pygame
from pygame.locals import *


class Person(pygame.sprite.Sprite):

    def __init__(self):
        super(Person, self).__init__()
        self.image = pygame.image.load("images\image001.png").convert()
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.image = pygame.transform.scale(self.image, (600, 600))
        self.rect = self.image.get_rect()
        self.pics = ["images\image001.png", "images\image002.png", "images\image003.png", "images\image004.png", "images\image005.png", "images\image006.png", "images\image007.png"]

    def hang(self, wrong_guesses):
        print("hanging is happening")
        self.image = pygame.image.load(self.pics[wrong_guesses]).convert()
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.image = pygame.transform.scale(self.image, (600, 600))



