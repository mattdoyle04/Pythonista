from scene import *
import ui
import sound
import random
import math
import appex

A = Action
width, height = ui.get_screen_size()

answer = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes', 'Signs point to yes', 'Reply hazy try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', 'Dont count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']

class MyScene (Scene):
	def setup(self):
		self.bounds = (0,400)
		self.background_color = 'white'
		self.move_balls = False
		self.balls_moved = 0
		
		self.b_ball = ShapeNode(path = ui.Path.oval(0,0,width/2,width/2), fill_color = 'black', position = (width/2,height/2), parent = self)
		
		self.i_ball = SpriteNode('shp:sun', position = (self.size.w/2,self.size.h/2), scale = 1, color = '#000066', parent = self)
		
		self.label = LabelNode('8Ball', font = ('Arial',14), position = (self.size.w/2,self.size.h/2), color='white', alpha = 0, parent = self)
	
	def update(self):
		pass
				
	def touch_began(self, touch):
		self.movement()
			
	def movement(self):
		self.label.alpha = 0
		speed = .22
		x_one, y_one = random.randint(-150,150), random.randint(-150,150)
		x_two, y_two = random.randint(-150,150), random.randint(-150,150)
		x_three, y_three = random.randint(-150,150), random.randint(-150,150)
		
		self.b_ball.run_action(A.sequence(
			A.move_by(x_one,y_one,speed,TIMING_EASE_OUT_2),
			A.move_by(-x_one,-y_one,speed,TIMING_EASE_OUT_2),
			A.move_by(x_two, y_two,speed,TIMING_EASE_OUT_2),
			A.move_by(-x_two, -y_two,speed,TIMING_EASE_OUT_2),
			A.move_by(x_three,y_three,speed,TIMING_EASE_OUT_2),
			A.move_by(-x_three,-y_three,speed,TIMING_EASE_OUT_2)))
		self.i_ball.run_action(A.sequence(
			A.move_by(x_one,y_one,speed,TIMING_EASE_OUT_2),
			A.move_by(-x_one,-y_one,speed,TIMING_EASE_OUT_2),
			A.move_by(x_two, y_two,speed,TIMING_EASE_OUT_2),
			A.move_by(-x_two, -y_two,speed,TIMING_EASE_OUT_2),
			A.move_by(x_three,y_three,speed,TIMING_EASE_OUT_2),
			A.move_by(-x_three,-y_three,speed,TIMING_EASE_OUT_2)))
		self.label.run_action(A.sequence(
			A.move_by(x_one,y_one,speed,TIMING_EASE_OUT_2),
			A.move_by(-x_one,-y_one,speed,TIMING_EASE_OUT_2),
			A.move_by(x_two, y_two,speed,TIMING_EASE_OUT_2),
			A.move_by(-x_two, -y_two,speed,TIMING_EASE_OUT_2),
			A.move_by(x_three,y_three,speed,TIMING_EASE_OUT_2),
			A.move_by(-x_three,-y_three,speed,TIMING_EASE_OUT_2)))
			
		rand = random.randint(0, 20)				
		answer_str = answer[rand-1]
		self.label.text = answer_str
		self.label.run_action(A.fade_to(1,2.5))

run(MyScene())


