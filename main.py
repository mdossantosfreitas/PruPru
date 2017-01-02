#!/usr/bin/env python

from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
from pygame.locals import *
from Character import *
from Texture import Texture 
import random
from Level import Level

class Main():
	limit_x = 7
	limit_y = 5
	init_x = -8
	init_y = -5
	key = 0
	time = 0
	count = 1
	next_level = 1
	def resize(self,(width, height)):
		if height==0:
			height=1
		glViewport(0, 0, width, height)
		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		gluOrtho2D(-8.0, 8.0, -6.0, 6.0)
		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()

	def init(self, qtd):
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
		self.mens_linha1 = []
		self.mens_linha2 = []
		self.mens_linha3 = []
		self.shits = []
		self.bordas = []
		self.create_mens(qtd)
		
		self.pomba = Pomba("data/pomba2.png", -1.0, -5.0, 1.0, 1.0)
		self.pontos = Sprite("data/pontos.png", -8.0, -6.0, 3, 0.9)
		self.tempo = Sprite("data/tempo.png", -2.8, -6.0, 3, 0.9)
		
		


		
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
			for men in self.mens_linha1:
				if(colision_b == False):
					colision_b = self.colision_up(self.pomba, men)
					
		 	for men in self.mens_linha2:
				if(colision_b == False):
					colision_b = self.colision_up(self.pomba, men)
					
			for men in self.mens_linha3:
				if(colision_b == False):
					colision_b = self.colision_up(self.pomba, men)
			
			if(colision_b == True):
				self.pomba.dead = True
			
		if kpb[pygame.K_DOWN]:
			if(self.pomba.y > self.init_y):
				self.pomba.y-=0.1
			
			for men in self.mens_linha1:
				if(colision_b == False):
					colision_b = self.colision_down(self.pomba, men)
					
			for men in self.mens_linha2:
				if(colision_b == False):
					colision_b = self.colision_down(self.pomba, men)
					
			for men in self.mens_linha3:
				if(colision_b == False):
					colision_b = self.colision_down(self.pomba, men)
			
	  	if(colision_b == True):
				self.pomba.dead = True
		
		if kpb[pygame.K_RIGHT]:
			if(self.pomba.x < self.limit_x):
				self.pomba.x+=0.1
				
			for men in self.mens_linha1:
				if(colision_b == False):
					colision_b = self.colision_right(self.pomba, men)
					
		 	for men in self.mens_linha2:
				if(colision_b == False):
					colision_b = self.colision_right(self.pomba, men)
			
			for men in self.mens_linha3:
				if(colision_b == False):
					colision_b = self.colision_right(self.pomba, men)
			
			if(colision_b == True):
				self.pomba.dead = True
	
		if kpb[pygame.K_LEFT]:
			if(self.pomba.x > self.init_x):
				self.pomba.x-=0.1
			for men in self.mens_linha1:
				if(colision_b == False):
					colision_b = self.colision_left(self.pomba, men)
					
			for men in self.mens_linha2:
				if(colision_b == False):
					colision_b = self.colision_left(self.pomba, men)
					
			for men in self.mens_linha3:
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
		
		self.ganhou = True
		while(self.ganhou == True):
			self.ganhou = False
			print "entrei"
			self.level_number = self.next_level
			time2 = self.next_level * 3
			time3 = time2/6
			time2 = time2%6
			self.level = Level(self.next_level, self.next_level * 3, time3, time2, 0)
			self.init(self.next_level * 3)
			
			clock = pygame.time.Clock()
			while(self.level.passou_tempo() == False and self.level.ganhou == False):
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
				
				self.next_level +=1
				if(self.level.ganhou == True):
					self.ganhou = True
					
			self.flush()
				
			
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
			posy = 2
			if(i == 0):
				visible = True
			else:
				visible = False
			men_obj1 = Men("data/men1.jpg", posx, posy, 1.0, 1.0, visible)
			posx = random.uniform(-8.0, 3.0)
			posy = 3.5
			men_obj2 = Men("data/men1.jpg", posx, posy, 1.0, 1.0, visible)
			posx = random.uniform(-8.0, 3.0)
			posy = 5
			men_obj3 = Men("data/men1.jpg", posx, posy, 1.0, 1.0, visible)
		
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
			shit.y +=shit.speed
		
		shits2 = self.shits
		mens2 = self.mens_linha1
		for shit in shits2:
			for men in mens2:
				if(self.colision(shit, men) == True):
					self.level.increaseKill()
					self.mens_linha1.remove(men)
					self.shits.remove(shit)
					self.pomba.points += 1
					if(self.pomba.points == 10):
						self.pomba.points = 0
						self.pomba.points2 +=1
			
						
		shits2 = self.shits
		mens2 = self.mens_linha2
		for shit in shits2:
			for men in mens2:
				if(self.colision(shit, men) == True):
					self.level.increaseKill()
					self.mens_linha2.remove(men)
					self.shits.remove(shit)
					self.pomba.points += 1
					if(self.pomba.points == 10):
						self.pomba.points = 0
						self.pomba.points2 +=1
			
						
		shits2 = self.shits
		mens2 = self.mens_linha3
		for i in range(0, len(self.shits)):
			for men in mens2:				
				if(self.colision(shit, men) == True):
					self.level.increaseKill()
					self.mens_linha3.remove(men)
					self.shits.remove(shit)
					self.pomba.points += 1
					if(self.pomba.points == 10):
						self.pomba.points = 0
						self.pomba.points2 +=1
	 
			
		if(self.level.c_kills == self.level.n_kills):
			self.level.ganhou = True
			
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
	
	