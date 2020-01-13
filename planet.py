import math

'''
This module implements a planet Class

'''

class Planet (object):

	def __init__(self, name, radius, distance):
		""" Initializes the instance variables"""

		self.name     = name
		self.radius   = radius 
		self.distance = distance

	def getName(self):
		''' Returns the name of the planet'''
		return self.name

	def getRadius(self):
		''' Returns the radius of the planet'''
		return self.radius

	def getDistance(self):
		''' Returns the distance of the planet
		    from the sun
		'''
		return self.distance

	def calcVolume(self):
		''' Calculates the volume of the planet'''
		volume = (4.0/3) * math.pi * (self.radius ** 3)
		return volume

	def updateName(self,name):
		''' Changes or sets the name of the planet'''
		self.name = name


