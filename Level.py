# -*- coding: utf-8 -*-
"""
Created on Mon Jan 02 12:26:26 2017

@author: Matheus
"""

class Level():
	level = 0
	n_kills = 0
	c_kills = 0
	c_time1 = 0
	c_time2 = 0
	c_time3 = 0
	l_time1 = 0
	l_time2 = 0
	l_time3 = 0
	
	
	alive = True
	ganhou = False
	def __init__(self, level, kills, l_1, l_2, l_3):
		self.n_kills = kills
		self.level = level
		self.l_time1 = l_1
		self.l_time2 = l_2
		self.l_time3 = l_3
	
	def increaseKill(self):
		self.c_kills +=1
		
	def increaseTime1(self):
		self.time1 +=1
		
	def increaseTime2(self):
		self.time2 +=1
		
	def increaseTime3(self):
		self.time3 +=1
	
	def perdeu(self):
		self.alive = False
		
	def passou_tempo(self):
		boo = False
		if(self.c_time3 == self.l_time3):
			if(self.c_time2 == self.l_time2):
				if(self.c_time1 == (self.l_time1+1)):
					boo = True
		return boo		
		
	
	