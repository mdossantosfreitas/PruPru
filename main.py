#!/usr/bin/env python

from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
from pygame.locals import *
from Character import *
from Borda import Borda
from Texture import Texture 
import random

class Main():
	limit_x = 7
	limit_y = 5
	init_x = -8
	init_y = -5
	key = 0
	
	def resize(self,(width, height)):
		if height==0:
			height=1
		glViewport(0, 0, width, height)
		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		gluOrtho2D(-8.0, 8.0, -6.0, 6.0)
		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()

	def init(self):
		#set some basic OpenGL settings and control variables
		glShadeModel(GL_SMOOTH)
		glClearColor(0.0, 0.0, 0.0, 0.0)
		glClearDepth(1.0)
		glDisable(GL_DEPTH_TEST)
		glDisable(GL_LIGHTING)
		glDepthFunc(GL_LEQUAL)
		glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)
		glEnable(GL_BLEND)

		self.demandedFps=30.0
		self.done=False

		self.x_pomba,self.y_pomba=-1.0,-6.0
		self.mens = []
		self.shits = []
		self.bordas = []
		self.create_mens(3)
		
		self.pomba = Pomba("data/pomba2.png", -1.0, -5.0, 1.0, 1.0)
		self.pontos = Sprite("data/pontos.png", -8.0, -6.0, 3, 0.9)
		
		


		
	def draw(self):
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		glLoadIdentity()
		glDisable(GL_LIGHTING)
		glEnable(GL_TEXTURE_2D)
		glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

		if(self.pomba.dead == False):
			
			#draw_pigeon
			glPushMatrix()
			glTranslatef(self.pomba.x, self.pomba.y, 0.0)
			glColor4f(1.0, 1.0, 1.0,1.0)
			self.pomba.draw()
			glPopMatrix()
			
			#draw_mens
			self.draw_mens()
			
			#draw_shits
			self.draw_shits()
			
	
 		#	self.draw_borda()
			self.draw_pontos()	
		 	if(self.pomba.points == 0):
				self.pt = Sprite("data/0.png", -4.0, -6.0, 1, 0.9)
			if(self.pomba.points == 1):
				self.pt = Sprite("data/1.png", -4.0, -6.0, 1, 0.9)
			if(self.pomba.points == 2):
				self.pt = Sprite("data/2.png", -4.0, -6.0, 1, 0.9)
			if(self.pomba.points == 3):
				self.pt = Sprite("data/3.png", -4.0, -6.0, 1, 0.9)
		
			glPushMatrix()
			glTranslatef(self.pt.x, self.pt.y, 0.0)
			glColor4f(1.0, 1.0, 1.0,1.0)
			self.pt.draw()
			glPopMatrix()
			
					
				
		
					
			
	
	def draw_borda(self):
		for borda in self.bordas:
			glPushMatrix()							
			glTranslatef(borda.x, borda.y, 0.0)
			borda.draw()
			glPopMatrix()
			
	def draw_pontos(self):
			glPushMatrix()							
			glTranslatef(self.pontos.x, self.pontos.y, 0.0)
			self.pontos.draw()
			glPopMatrix()
			
	def Input(self):
		mpb=pygame.mouse.get_pressed() # mouse pressed buttons
		kpb=pygame.key.get_pressed() # keyboard pressed buttons
		msh=pygame.mouse.get_rel() # mouse shift

		if kpb[pygame.K_SPACE]:
			if(self.key == 0):
				shit = 	Shit("data/shit.jpg", self.pomba.x, self.pomba.y+self.pomba.size['height'], 1.0, 1.0)
				self.shits.append(shit)
				self.key +=1
			else:
				if(self.key == 4):
					self.key = 0
				else:
					self.key +=1
			
			

		colision_b = False
		if kpb[pygame.K_UP]:
			if(self.pomba.y < self.limit_y):
				self.pomba.y+=0.1
			for men in self.mens:
				if(colision_b == False):
					colision_b = self.colision_up(self.pomba, men)
			
			if(colision_b == True):
				self.pomba.dead = True
			
		if kpb[pygame.K_DOWN]:
			if(self.pomba.y > self.init_y):
				self.pomba.y-=0.1
			
			for men in self.mens:
				if(colision_b == False):
					colision_b = self.colision_down(self.pomba, men)
			
	  	if(colision_b == True):
				self.pomba.dead = True
		
		if kpb[pygame.K_RIGHT]:
			if(self.pomba.x < self.limit_x):
				self.pomba.x+=0.1
			for men in self.mens:
				if(colision_b == False):
					colision_b = self.colision_right(self.pomba, men)
			
			if(colision_b == True):
				self.pomba.dead = True
	
		if kpb[pygame.K_LEFT]:
			if(self.pomba.x > self.init_x):
				self.pomba.x-=0.1
			for men in self.mens:
				if(colision_b == False):
					colision_b = self.colision_left(self.pomba, men)
			
			if(colision_b == True):
				self.pomba.dead = True
	
	
		
		

	def __init__(self):

		video_flags = pygame.OPENGL|pygame.DOUBLEBUF

		pygame.init()
		pygame.display.set_mode((640,480), video_flags)

		pygame.display.set_caption("PruPru")

		self.resize((640,480))
		self.init()


		clock = pygame.time.Clock()
		while 1:
			event = pygame.event.poll()
			if event.type == pygame.QUIT or self.done:
				pygame.quit ()
				break
			
			self.update_shits()
			self.move_mens()
			self.Input()
			self.draw()

			pygame.display.flip()

			#limit fps
			clock.tick(self.demandedFps)
			
	def move(self, x, y, z):
		glPushMatrix()
		glTranslate(x, y, z)
		self.sprite1.draw()
		glPopMatrix()
		
	def colision_up(self, obj1, obj2):
		if(((obj1.x >= obj2.x) 	and (obj1.x <= (obj2.x+obj2.size['width'])))
    	or 	(((obj1.x+obj1.size['width']) >= obj2.x) 	and ((obj1.x+obj1.size['width']) <= (obj2.x+obj2.size['width'])))):
			if(((obj1.y+obj1.size['height']) >= obj2.y) and ((obj1.y+obj1.size['height']) <= obj2.y+obj2.size['height'])):				
				return True
			else:
				return False
		else:
			return False
			
	def colision_down(self, obj1, obj2):
		if(((obj1.x >= obj2.x) 	and (obj1.x <= (obj2.x+obj2.size['width']))) 	or 	(((obj1.x+obj1.size['width']) >= obj2.x) 	and ((obj1.x+obj1.size['width']) <= (obj2.x+obj2.size['width'])))):
			if((obj1.y <= (obj2.y+obj2.size['height'])) and (obj1.y >= obj2.y)):				
				return True
			else:
				return False
		else:
			return False

	def colision_left(self, obj1, obj2):
		if (((obj1.y >= obj2.y )	and (obj1.y <= (obj2.y+obj2.size['height']) ))		or 	(((obj1.y+obj1.size['height']) >= obj2.y) 	and ((obj1.y+obj1.size['height'] <= obj2.y+obj2.size['height'])))):
			if((obj1.x <= (obj2.x+obj2.size['width'])) and (obj1.x>= obj2.x)):
				return True
			else:
				return False
		else:
			return False
			
			
	def colision_right(self, obj1, obj2):
		if (((obj1.y >= obj2.y )	and (obj1.y <= (obj2.y+obj2.size['height']) ))		or 	(((obj1.y+obj1.size['height']) >= obj2.y) 	and ((obj1.y+obj1.size['height'] <= obj2.y+obj2.size['height'])))):
			if(((obj1.x+obj1.size['width']) >= obj2.x) and (obj1.x+obj1.size['width'] <= (obj2.x+obj2.size['width']))):
				return True
			else:
				return False
		else:
			return False
			
	
		

	def move_mens(self):
		for men in self.mens:
			if men.going_right == True:
				men.x += men.speed
				if men.x >= self.limit_x:
					men.x -= men.speed
	
					men.going_right = False
			else:
				if men.going_right == False:
					men.x -= men.speed
					if men.x <= self.init_x:
						men.x += men.speed
						men.going_right = True


			
	def create_mens(self, qtd):
		
		for i in range(0, qtd):
			posx = random.uniform(-8.0, 3.0)
			posy = 0.5 + (i+1)*1.5
			men_obj = Men("data/men1.jpg", posx, posy, 1.0, 1.0)
		
			self.mens.append(men_obj)
			
  
	def colision(self, obj1, obj2):
		if(self.colision_up(obj1, obj2) == True):
			return True
		else:
			if(self.colision_down(obj1, obj2) == True):
				return True
			else:
					if(self.colision_left(obj1, obj2) == True):
						return True
					else:
							if(self.colision_right(obj1, obj2) == True):
								return True
							else:
								return False
		
	def draw_mens(self):
		for men in self.mens:
			glPushMatrix()
			glTranslatef(men.x, men.y, 0.0)
			glColor4f(1.0, 1.0, 1.0,1.0)
			men.draw()
			glPopMatrix()
			
	def draw_shits(self):
		for shit in self.shits:
			glPushMatrix()
			glTranslatef(shit.x, shit.y, 0.0)
			glColor4f(1.0, 1.0, 1.0,1.0)
			shit.draw()
			glPopMatrix()
			
	def update_shits(self):
		for shit in self.shits:
			shit.y +=shit.speed
			
		shits2 = self.shits
		mens2 = self.mens
		for shit in shits2:
			for men in mens2:
				if(self.colision(shit, men) == True):
					self.mens.remove(men)
					self.shits.remove(shit)
					self.pomba.points += 1
			


		
if __name__ == '__main__': Main()
	
	