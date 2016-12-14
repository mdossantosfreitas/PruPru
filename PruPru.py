# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 20:46:15 2016

@author: Matheus
"""

from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
from pygame.locals import *
import sys

background = pygame.image.load("data/city.jpeg")
backgroundRect = background.get_rect()

size = (width, height) = background.get_size()
screen = pygame.display.set_mode((1000, 500))

while 1:
     for event in pygame.event.get():
       if event.type == pygame.QUIT: sys.exit() 
       screen.blit(background, backgroundRect)          
       pygame.display.flip()
	  