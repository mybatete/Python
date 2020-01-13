'''
This module implements an aircraft Class
And inherits a vehicle class
'''

from vehicle import Vehicle

class Aircraft (Vehicle):

	def __init__(self, name, owner, registration, speed, \
			altitude, cruiseSpeed,stallSpeed, engines):
		""" Initializes the instance variables"""

		self.altitude    = altitude
		self.cruiseSpeed = cruiseSpeed
		self.stallSpeed  = stallSpeed
		self.engines     = engines

		Vehicle.__init__(self, name, owner, registration, speed)

	def getEngines(self):
		''' Returns the number of engines'''
		return self.engines

	def getstallSpeed(self):
		''' Returns the stall speed of the aircraft'''
		return self.stallSpeed


