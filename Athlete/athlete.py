import math

'''
This module implements an athlete Class
It records the performance of athletes.

'''

class Athlete (object):

	def __init__(self, num ,name, height, weight, trial1, trial2, trial3):
		""" Initializes the instance variables"""

		self.num    = num
		self.name   = name
		self.height = height  
		self.weight = weight  
		self.time   = []

		self.time.append(trial1) 
		self.time.append(trial2) 
		self.time.append(trial3) 

	def getNum(self):
		''' Returns the ID number of the athlete'''
		return self.num

	def getName(self):
		''' Returns the name of the athlete'''
		return self.name

	def getHeight(self):
		''' Returns the height of the athlete'''
		return self.height

	def getWeight(self):
		''' Returns the weight of the athlete'''
		return self.weight

	def averageTime(self):
		''' Calculates the average time performance of the athlete'''

		total = 0

		for item in self.time:
			total += item

		average = total/3.0
 
		return average

	def updateHeight(self,height):
		''' Updates the height of the athlete'''
		self.height = height

	def updateWeight(self,weight):
		''' Updates the weight of the athlete'''
		self.weight = weight


