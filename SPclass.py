#!/bin/python3

import os
import random
import math
from tkinter import *

HEIGHT = 500
WIDTH = 1000

root = Tk() 
root.title("SpSh") #Название окна
c = Canvas(root, width=WIDTH, height=HEIGHT, background="#001300") #Создание окна
c.pack()

class SpSh(): #Клас "космический корабль"
	speed = 0
	corner = 270 #Угол отклонения носа корабля
	corner_move = 270 #Направление движения
	coordx = 0
	coordy = 0
	def hit(self,value): #Нанесение урона
		print('{}: FIRE!'.format(self.name))
		self.hp -= value
		if self.hp < 0:
			self.hp = 0
		print('{}: HIT({}). I have {}'.format(self.name,value,self.hp))
		if self.hp <= 0:
			print("{}: You kill me, bastard!".format(self.name))
		else:
			print("{}: I'm still alive".format(self.name))
			
	def change_ungle(self,key):
		if key == 'a':
			self.corner += self.turn_speed
			if self.corner >= 360: 
				self.corner = 0
		elif key == 'd':
			self.corner -= self.turn_speed
			if self.corner <= -360: 
				self.corner = 0
		elif key == 'w':
			if self.speed < self.maxspeed: 
				self.speed += 1
		left,up,right,down = c.coords(self.SH)	
		c.delete(self.SH)
		self.SH = c.create_arc(left,up,right,down, start = self.corner - (self.extent_sh/2), extent = self.extent_sh, fill = "#006350", outline = "white")	
		
	def press_key(self,press): #
		if press.keysym == "w": 
			self.change_ungle('w')
		elif press.keysym == "a": 
			self.change_ungle('a')
		elif press.keysym == "d":
			self.change_ungle('d')
		elif press.keysym == "s": 
			#if self.speed > 0: 
				#self.speed -= 1
			pass
		self.move_sh()
		
	def move_sh(self): #
		sub_ungle = (self.corner_move - self.corner)/2
		#sub_cos = abs(math.cos(math.radians(self.corner_move)) - math.cos(math.radians(self.corner)))
		#sub_sin = abs(math.sin(math.radians(self.corner_move)) + math.sin(math.radians(self.corner)))
		#self.speed = self.speed * math.sin(math.radians(sub_ungle))
		#if sub_ungle > 0: 
		#	self.corner_move = self.corner_move + sub_ungle * sub_cos 
		if sub_ungle < 0:
			self.corner_move = self.corner_move + abs(sub_ungle)
		else:
			self.corner_move = self.corner_move - abs(sub_ungle)
		self.coordx_change = -(self.coordx_change + self.speed * math.cos(math.radians(self.corner_move)))
		self.coordy_change = -(self.coordy_change - self.speed * math.sin(math.radians(self.corner_move)))
		
		c.move(self.SH,self.coordx_change,self.coordy_change)

class titan(SpSh): #
    typeofsh = 'Titan'
    hp = 20000 #
    maxspeed = 10.0 #
    weight = 8000 #
    mindamage = 1500 #
    maxdamage = 3000 #
    SH_RAD = 20 #
    extent_sh = 35 #Размер корабля
    coordx_change = 0 #random.randint(-5,0)
    coordy_change = 0 #5
    turn_speed = 5 #
    SH = c.create_arc((WIDTH/2-SH_RAD,HEIGHT/2-SH_RAD), (WIDTH/2+SH_RAD,HEIGHT/2+SH_RAD), start = 270 - (extent_sh/2), extent = extent_sh, fill = "#006350", outline = "white")
    #SH = c.create_polygon((WIDTH/2,HEIGHT/2-SH_RAD,
	#						WIDTH/2+SH_RAD/2,HEIGHT/2+SH_RAD/2,
	#						WIDTH/2-SH_RAD/2,HEIGHT/2+SH_RAD/2), outline = "white", fill = "#006350")
	
    def __init__(self,name):
        self.name = name
        #print(c.coords(self.SH))
        #print('My name is {}. My type is Titan'.format(self.name))
        
class lincore(SpSh): #
    typeofsh = 'Lincore'
    hp = 10000
    maxspeed = 6.0
    weight = 3000
    mindamage = 2000
    maxdamage = 4000
    SH_RAD = 20
    extent_sh = 25
    coordx_change = -5
    coordy_change = random.randint(-5,0)
    turn_speed = 5
    SH = c.create_oval(WIDTH/2-SH_RAD/2,HEIGHT/2-SH_RAD/2,WIDTH/2+SH_RAD/2,HEIGHT/2+SH_RAD/2, fill="white")
    def __init__(self,name):
        self.name = name
        print('My name is {}. My type is Lincore'.format(self.name))

class meteor: #
    RAD = random.randint(10,20)
    speed = random.randint(5,10)
    coordx = random.randint(20,WIDTH-20)
    coordy = random.randint(20,HEIGHT-20)
    coordx_change = random.randint(-10,10)
    coordy_change = random.randint(-10,10)
    bounce = False
    METEOR =  c.create_oval(coordx-RAD/2,coordy-RAD/2,coordx+RAD/2,coordy+RAD/2, fill="brown")
    def __inin__(self,name):
        self.name = name
        print('i\'m {}'.format(self.name))
    def move_met(self): #
        left,up,right,down = c.coords(self.METEOR)
        #print('LEFT: {}, UP: {}, RIGHT: {}, DOWN: {}, bounce: {}'.format(left,up,right,down,self.bounce))
        if ((((up) <= 0) or ((down) >= HEIGHT)) and (self.bounce == False)): 
            self.coordy_change = -self.coordy_change
            self.bounce = True
        elif ((((left) <= 0) or ((right) >= WIDTH)) and (self.bounce == False)): 
            self.coordx_change = -self.coordx_change
            self.bounce = True
        else:
            if (up > 0) and (down < HEIGHT) and (left > 0) and (right < WIDTH):
                self.bounce = False
        c.move(self.METEOR,self.coordx_change,self.coordy_change)
        
class Log:
	def __init__(self):
		self.x = 80
		self.y = 20
		#print(self.value)
	def drow_text(self, dictionary):
		
		self.area = []
		self.i = 0
		self.j = 0
		keys = dictionary.keys()
		for self.i in keys:
			self.txt = c.create_text(self.x,self.y,text = '',font = "Arial 14", fill = "white")
			self.area.append(self.txt)
			self.y += 20
	def update_text(self, new_dictionary):
		count = 0
		self.new_dictionary = new_dictionary
		keys = new_dictionary.keys()
		for self.j in keys:
			c.itemconfig(self.area[count],text = self.j + ' = ' + str(new_dictionary.get(self.j)))
			count += 1

def main_move_loop(): #
    global diction
    sh1.move_sh()
    #sh2.move_sh()
    met.move_met()
    #diction = {'Angle':sh1.corner, 'Speed':round(sh1.speed,1), 'Sin':round(math.sin(math.radians(sh1.corner)),2), 'Cos':round(math.cos(math.radians(sh1.corner)),2)}
    lg.update_text(diction)
    diction.clear()
    root.after(10,main_move_loop)


sh1 = titan('Thor')
#sh2 = lincore('Loki')
met = meteor()
lg = Log()
diction = {'Angle':sh1.corner, 'Speed':round(sh1.speed,1), 'Sin':round(math.sin(math.radians(sh1.corner)),2), 'Cos':round(math.cos(math.radians(sh1.corner)),2)}
lg.drow_text(diction)

c.focus_set() #
c.bind("<KeyPress>", sh1.press_key) #
main_move_loop()
root.mainloop() #
