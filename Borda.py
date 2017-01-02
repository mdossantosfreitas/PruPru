# -*- coding: utf-8 -*-
"""
Created on Sun Jan 01 23:08:30 2017

@author: Matheus
"""
from OpenGL.GL import *
from OpenGL.GLU import *
from Texture import Texture
		
class Borda():
	texture = None
	position = {'x': 0.0,
                'y': 0.0}
	size = {'width': 1.0,
            'height': 1.0}
	x = 0
	y = 0
												
	visible = False
	
												
	def __init__(self, texture_filename, position_x, position_y, width, height):
		self.texture = Texture(texture_filename)
		self.x = position_x
		self.y = position_y
		self.size['width'] = width
		self.size['height'] = height

	def draw(self):
		glBindTexture(GL_TEXTURE_2D, self.texture.texID)

		glBegin(GL_QUADS)
		
		posx = self.position['x']
		posy = self.position['y'] + self.size['height']	
		glTexCoord2f(0.0, 1.0)
		glVertex2f(posx, posy)
		
		posx = self.position['x'] + self.size['width']
		posy = self.position['y'] + self.size['height']
		glTexCoord2f(1.0, 1.0)
		glVertex2f(posx, posy)

		posx = self.position['x'] + self.size['width']
		posy = self.position['y']
		glTexCoord2f(1.0, 0.0)
		glVertex2f(posx, posy)
		
		posx = self.position['x']
		posy = self.position['y']
		glTexCoord2f(0.0, 0.0)
		glVertex2f(posx, posy)

		glEnd()		
  
