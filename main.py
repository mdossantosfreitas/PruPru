#!/usr/bin/env python

from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
from pygame.locals import *
from Character import *
from Texture import Texture 
import random
from Level import Level
import sys
import time

class Main():
	limit_x = 7
	limit_y = 5
	init_x = -8
	init_y = -5
	key = 0
	time = 0
	count = 1
	next_level = 1
	speed = 0.1
	esc = False
	final = False
	inicio = False
	NUMBER_OF_MEN = '1234'
	def resize(self,(width, height)):
		if height==0:
			height=1
		glViewport(0, 0, width, height)
		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		gluOrtho2D(-8.0, 8.0, -6.0, 6.0)
		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()
 
	def init_gl(self):
		#set some basic OpenGL settings and control variables
		glShadeModel(GL_SMOOTH)
		glClearColor(0.0, 0.0, 0.0, 0.0)
		glClearDepth(1.0)
		glDisable(GL_DEPTH_TEST)
		glDisable(GL_LIGHTING)
		glDepthFunc(GL_LEQUAL)
		glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)
		glEnable(GL_BLEND)
		
	def init(self, qtd):
		self.init_gl()
		
		self.done=False

		self.x_pomba,self.y_pomba=-1.0,-6.0
		self.mens_linha1 = []
		self.mens_linha2 = []
		self.mens_linha3 = []
		self.shits = []
		self.bordas = []
		self.create_mens(qtd)
		
		self.bg = Background("data/bg.png", -8, -5, 16, 11)
		self.pontos = Sprite("data/Points.png", -8.0, -6.0, 3, 0.9)
		self.tempo = Sprite("data/Time.png", -2.8, -6.0, 3, 0.9)
	
		self.pomba = Pomba("data/Pigeon.png", 1, 5, 1.0, 1.0)
		
		
		


		
	def draw(self):
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		glLoadIdentity()
		glDisable(GL_LIGHTING)
		glEnable(GL_TEXTURE_2D)
		glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
		
		if(self.inicio == False):
			if(self.final == False):
				if(self.pomba.dead == False):
					
					glPushMatrix()
					glTranslatef(self.bg.x, self.bg.y, 0.0)
					glColor4f(1.0, 1.0, 1.0,1.0)
					self.bg.draw()
					glPopMatrix()
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
						self.pt = Numero("data/0.png", -3.9, -6.0, 1, 0.9)
					if(self.pomba.points == 1):
						self.pt = Numero("data/1.png", -3.9, -6.0, 1, 0.9)
					if(self.pomba.points == 2):
						self.pt = Numero("data/2.png", -3.9, -6.0, 1, 0.9)
					if(self.pomba.points == 3):
						self.pt = Numero("data/3.png", -3.9, -6.0, 1, 0.9)
					
					glPushMatrix()
					glTranslatef(self.pt.x, self.pt.y, 0.0)
					glColor4f(1.0, 1.0, 1.0,1.0)
					self.pt.draw()
					glPopMatrix()
					
				 	if(self.pomba.points2 == 0):
						self.pt2 = Numero("data/0.png", -4.9, -6.0, 1, 0.9)
					if(self.pomba.points2 == 1):
						self.pt2 = Numero("data/1.png", -4.9, -6.0, 1, 0.9)
					if(self.pomba.points2 == 2):
						self.pt2 = Numero("data/2.png", -4.9, -6.0, 1, 0.9)
					if(self.pomba.points2 == 3):
						self.pt2 = Numero("data/3.png", -4.9, -6.0, 1, 0.9)
				
					glPushMatrix()
					glTranslatef(self.pt2.x, self.pt2.y, 0.0)
					glColor4f(1.0, 1.0, 1.0,1.0)
					self.pt2.draw()
					glPopMatrix()
					
					glPushMatrix()
					glTranslatef(self.tempo.x, self.tempo.y, 0.0)
					glColor4f(1.0, 1.0, 1.0,1.0)
					self.tempo.draw()
					glPopMatrix()
					
					path3 = self.get_number(self.level.c_time3)
					self.time3 = Numero(path3, 0.2, -6.0, 1, 0.9)
					
					glPushMatrix()
					glTranslatef(self.time3.x, self.time3.y, 0.0)
					glColor4f(1.0, 1.0, 1.0,1.0)
					self.time3.draw()
					glPopMatrix()
					
					path2 = self.get_number(self.level.c_time2)
					self.time2 = Numero(path2, 1.2, -6.0, 1, 0.9)
					
					glPushMatrix()
					glTranslatef(self.time2.x, self.time2.y, 0.0)
					glColor4f(1.0, 1.0, 1.0,1.0)
					self.time2.draw()
					glPopMatrix()
					
					path1 = self.get_number(self.level.c_time1)
					self.time1 = Numero(path1, 2.2, -6.0, 1, 0.9)
					
					glPushMatrix()
					glTranslatef(self.time1.x, self.time1.y, 0.0)
					glColor4f(1.0, 1.0, 1.0,1.0)
					self.time1.draw()
					glPopMatrix()
			else:
			
				glPushMatrix()
				glTranslatef(self.pontos.x, self.pontos.y, 0.0)
				glColor4f(1.0, 1.0, 1.0,1.0)
				self.pontos.draw()
				glPopMatrix()
			''''
		else:
	
			glPushMatrix()
			glTranslatef(self.enter.x, self.enter.y, 0.0)
			glColor4f(1.0, 1.0, 1.0,1.0)
			self.enter.draw()
			glPopMatrix()
			'''''
	
			
	def draw_pontos(self):
			glPushMatrix()							
			glTranslatef(self.pontos.x, self.pontos.y, 0.0)
			self.pontos.draw()
			glPopMatrix()
			
	def input2(self):
		mpb=pygame.mouse.get_pressed() # mouse pressed buttons
		kpb=pygame.key.get_pressed() # keyboard pressed buttons
		msh=pygame.mouse.get_rel() # mouse shift

		if kpb[pygame.K_SPACE]:
			self.esc = True
			self.inicio = False
			print "entrei"
					
	def Input(self):
		mpb=pygame.mouse.get_pressed() # mouse pressed buttons
		kpb=pygame.key.get_pressed() # keyboard pressed buttons
		msh=pygame.mouse.get_rel() # mouse shift

		if kpb[pygame.K_SPACE]:
			if(self.key == 0):
				shit = 	Shit("data/shit.png", self.pomba.x, self.pomba.y, 1.0, 1.0)
				if(self.colision_shits(shit) == False):
					self.shits.append(shit)
					self.key +=1
			else:
				if(self.key == 4):
					self.key = 0
				else:
					self.key +=1
			
		if kpb[pygame.K_RIGHT]:
			if(self.pomba.x < self.limit_x):
				self.pomba.x+=0.1
 

		if kpb[pygame.K_LEFT]:
			if(self.pomba.x > self.init_x):
				self.pomba.x-=0.1
				
		

	def __init__(self):
  
		iterator = 1
		video_flags = pygame.OPENGL|pygame.DOUBLEBUF

		pygame.init()
		pygame.display.set_mode((640,480), video_flags)

		pygame.display.set_caption("PruPru")
		self.resize((640,480))
		
		self.ganhou = True
		self.speed = 0.1
		
		
		clock = pygame.time.Clock()
		
		self.demandedFps=30.0		
		while(self.ganhou == True):
			self.final = False
			self.time = 0
			self.ganhou = False
		#	print "entrei"
			self.level_number = self.next_level
			self.level = Level(1, 3, 0, 3, 0)
			self.init(3)
			iterator +=1
			
			while(self.level.passou_tempo() == False):
				event = pygame.event.poll()
				if event.type == pygame.QUIT or self.done:
					pygame.quit()
					break
				
				self.Input()
				self.draw()
				self.move_mens()				
				self.update_shits()

				pygame.display.flip()
			
				if self.time == (30 * self.count):
					self.time = 0
					self.level.c_time1 +=1
				if(self.level.c_time1 == 10):
					self.level.c_time1 = 0
					self.level.c_time2 +=1
				if(self.level.c_time2 == 7):
					self.level.c_time2 = 0
					self.level.c_time3 +=1
				self.time +=1

			#limit fps
				clock.tick(self.demandedFps)
			self.flush() 
			self.ganhou = False
		
				
		time.sleep(3)
		pygame.display.quit()
		pygame.quit() 
		sys.exit(0)
		
	def move(self, x, y, z):
		glPushMatrix()
		glTranslate(x, y, z)
		self.sprite1.draw()
		glPopMatrix()
	
	def colision_shits(self, shit):
		coli = False
		for sh in self.shits:
			if(self.colision(shit, sh)):
				coli = True
		return coli
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
		for men in self.mens_linha1:
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
						
		for men in self.mens_linha2:
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
		
		for men in self.mens_linha3:
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
		qtd = qtd/3
		for i in range(0, qtd):
			posx = random.uniform(-8.0, 3.0)
			posy = -5
			if(i == 0):
				visible = True
			else:
				visible = False
			sprite = random.choice(self.NUMBER_OF_MEN)
			men_obj1 = Men("data/cit%s.png" % (sprite), posx, posy, 1.0, 1.0, visible, self.speed)
			posx = random.uniform(-8.0, 3.0)
			posy = -3.5
			sprite = random.choice(self.NUMBER_OF_MEN)
			men_obj2 = Men("data/cit%s.png" % (sprite), posx, posy, 1.0, 1.0, visible, self.speed)
			posx = random.uniform(-8.0, 3.0)
			posy = -2
			sprite = random.choice(self.NUMBER_OF_MEN)
			men_obj3 = Men("data/cit%s.png" % (sprite), posx, posy, 1.0, 1.0, visible, self.speed)
		
			self.mens_linha1.append(men_obj1)
			self.mens_linha2.append(men_obj2)
			self.mens_linha3.append(men_obj3)
			
  
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
		for men in self.mens_linha1:
			if(men.visible == True):
				glPushMatrix()
				glTranslatef(men.x, men.y, 0.0)
				glColor4f(1.0, 1.0, 1.0,1.0)
				men.draw()
				glPopMatrix()
			
		for men in self.mens_linha2:
			if(men.visible == True):			
				glPushMatrix()
				glTranslatef(men.x, men.y, 0.0)
				glColor4f(1.0, 1.0, 1.0,1.0)
				men.draw()
				glPopMatrix()
			
		for men in self.mens_linha3:
			if(men.visible == True):			
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
			shit.y -=shit.speed
			
			if(len(self.mens_linha3) > 0):
				coli = False
				shits2 = self.shits
				
				for shit in shits2:
					if(coli == False):
						men = self.mens_linha3[0]
						if(self.colision(shit, men) == True):
							self.level.increaseKill()
							x = self.mens_linha3.pop()
							y = self.shits.pop()
							coli = True
							self.pomba.points += 1
							if(self.pomba.points == 10):
								self.pomba.points = 0
								self.pomba.points2 +=1
				if(coli == True):			
					sprite = random.choice(self.NUMBER_OF_MEN)
					posx = random.uniform(-8.0, 3.0)
					posy = -2
					men_obj3 = Men("data/cit%s.png" % (sprite), posx, -2, 1.0, 1.0, True, self.speed)
					self.mens_linha3.append(men_obj3)
					self.speed = self.speed + 0.01
				
			if(len(self.mens_linha2) > 0):
				coli = False
				shits2 = self.shits
			
				for shit in shits2:
					if(coli == False):
						men = self.mens_linha2[0]
						if(self.colision(shit, men) == True):
							self.level.increaseKill()
							x = self.mens_linha2.pop()
							y = self.shits.pop()
							coli = True
							self.pomba.points += 1
							if(self.pomba.points == 10):
								self.pomba.points = 0
								self.pomba.points2 +=1
				if(coli == True):			
					sprite = random.choice(self.NUMBER_OF_MEN)
					posx = random.uniform(-8.0, 3.0)
					posy = -3.5
					men_obj2 = Men("data/cit%s.png" % (sprite), posx, -3.5, 1.0, 1.0, True, self.speed)
					self.mens_linha2.append(men_obj2)
					self.speed = self.speed + 0.01
					
		if(len(self.mens_linha1) > 0):
			coli = False
			shits2 = self.shits
			
			for shit in shits2:
				if(coli == False):
					men = self.mens_linha1[0]
					if(self.colision(shit, men) == True):
						self.level.increaseKill()
						x = self.mens_linha1.pop()
						y = self.shits.pop()
						coli = True
						self.pomba.points += 1
						if(self.pomba.points == 10):
							self.pomba.points = 0
							self.pomba.points2 +=1
			if(coli == True):			
				sprite = random.choice(self.NUMBER_OF_MEN)
				posx = random.uniform(-8.0, 3.0)
				posy = -5
				men_obj1 = Men("data/cit%s.png" % (sprite), posx, -5, 1.0, 1.0, True, self.speed)
				self.mens_linha1.append(men_obj1)
				self.speed = self.speed + 0.01
			
	def get_number(self, number):
		if(number == 0):
			return "data/0.png"
		if(number == 1):
			return "data/1.png"
		if(number == 2):
			return "data/2.png"
		if(number == 3):
			return "data/3.png"
		if(number == 4):
			return "data/4.png"
		if(number == 5):
			return "data/5.png"
		if(number == 6):
			return "data/6.png"
		if(number == 7):
			return "data/7.png"
		if(number == 8):
			return "data/8.png"
		if(number == 9):
			return "data/9.png"
		
	def flush(self):
		for i in range(len(self.shits)):
			x = self.shits.pop()
				
		for i in range(len(self.mens_linha1)):
			x = self.mens_linha1.pop()
			
		for i in range(len(self.mens_linha2)):
			x = self.mens_linha2.pop()
			
		for i in range(len(self.mens_linha3)):
			x = self.mens_linha3.pop()
				
if __name__ == '__main__': Main()
	
	