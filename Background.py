# -*- coding: utf-8 -*-
from OpenGL.GL import *
from OpenGL.GLU import *
import pygame, pygame.image
from pygame.locals import *
from Texture import Texture
from Compiler import Compiler

TEXDIR="data/textures/locations/"

class Background():
	def __init__(self,half_width,half_height,filename):
		self.compiler=Compiler()
		self.background_t = Texture(TEXDIR+filename)
		self.background_geom=self.compiler.quad(half_width,half_height)
		
	def draw(self):
		glPushMatrix()
		glBindTexture(GL_TEXTURE_2D,self.background_t.texID)
		glCallList(self.background_geom)
		glPopMatrix()
