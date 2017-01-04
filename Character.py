from OpenGL.GL import *
from OpenGL.GLU import *
from Texture import Texture

class Pomba():
	texture = None
	position = {'x': 0.0,
                'y': 0.0}
	size = {'width': 1.0,
            'height': 1.0}
	x = 0
	y = 0
												
	dead = False
	points = 0
	points2 = 0
												
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
		glTexCoord2f(posx, posy)
		glVertex2f(posx, posy)
		posx = self.position['x'] + self.size['width']
		posy = self.position['y'] + self.size['height']
		glTexCoord2f(posx, posy)
		glVertex2f(posx, posy)

		posx = self.position['x'] + self.size['width']
		posy = self.position['y']
		glTexCoord2f(posx, posy)
		glVertex2f(posx, posy)
		posx = self.position['x']
		posy = self.position['y']
		glTexCoord2f(posx, posy)
		glVertex2f(posx, posy)

		glEnd()
		
class Men():
	texture = None
	position = {'x': 0.0,
                'y': 0.0}
	size = {'width': 1.0,
            'height': 1.0}
												
	dead = False
	speed = 0.1
	going_right = True
	visible = False
	
												
	def __init__(self, texture_filename, position_x, position_y, width, height, visible, speed):
		self.texture = Texture(texture_filename)
		self.x= position_x
		self.y= position_y
		self.size['width'] = width
		self.size['height'] = height
		self.visible = visible
		self.speed = speed

	def draw(self):
		glBindTexture(GL_TEXTURE_2D, self.texture.texID)

		glBegin(GL_QUADS)

		posx = self.position['x']
		posy = self.position['y'] + self.size['height']
		glTexCoord2f(posx, posy)
		glVertex2f(posx, posy)
		posx = self.position['x'] + self.size['width']
		posy = self.position['y'] + self.size['height']
		glTexCoord2f(posx, posy)
		glVertex2f(posx, posy)

		posx = self.position['x'] + self.size['width']
		posy = self.position['y']
		glTexCoord2f(posx, posy)
		glVertex2f(posx, posy)
		posx = self.position['x']
		posy = self.position['y']
		glTexCoord2f(posx, posy)
		glVertex2f(posx, posy)

		glEnd()
		
		def increase_speed(self):
			self.speed += 0.01
		
class Shit():
	texture = None
	position = {'x': 0.0,
                'y': 0.0}
	size = {'width': 1.0,
            'height': 1.0}
	speed = 0.1
	visible = True
												
	def __init__(self, texture_filename, position_x, position_y, width, height):
		self.texture = Texture(texture_filename)
		self.x= position_x
		self.y = position_y
		self.size['width'] = width
		self.size['height'] = height

	def draw(self):
		glBindTexture(GL_TEXTURE_2D, self.texture.texID)

		glBegin(GL_QUADS)

		posx = self.position['x']
		posy = self.position['y'] + self.size['height']
		glTexCoord2f(posx, posy)
		glVertex2f(posx, posy)
		posx = self.position['x'] + self.size['width']
		posy = self.position['y'] + self.size['height']
		glTexCoord2f(posx, posy)
		glVertex2f(posx, posy)

		posx = self.position['x'] + self.size['width']
		posy = self.position['y']
		glTexCoord2f(posx, posy)
		glVertex2f(posx, posy)
		posx = self.position['x']
		posy = self.position['y']
		glTexCoord2f(posx, posy)
		glVertex2f(posx, posy)

		glEnd()
		
class Sprite():
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
  
class Numero():
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

		