'''
This module implements a vehicle Class
'''

class Vehicle (object):

	def __init__(self, name, owner, registration, speed):
		""" Initializes the instance variables"""

		self.name         = name
		self.owner        = owner
		self.registration = registration
		self.speed        = speed 

	def getName(self):
		''' Returns the name of the vehicle'''
		return self.name

	def getOwner(self):
		''' Returns the owner of the vehicle'''
		return self.owner

	def getSpeed(self):
		''' Returns the speed of the vehicle'''
		return self.speed

	def getRegistration(self):
		''' Returns the registration of the vehicle
		'''
		return self.registration

	def updateName(self,name):
		''' Changes or sets the name of the vehicle'''
		self.name = name


