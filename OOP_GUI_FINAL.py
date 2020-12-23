from tkinter import *
from tkinter import messagebox as msg

#First define the class

class App:

	#constructor
	def __init__(self, parent):#here:pass the tk object
		#Create a function to make all to make all the environments
		self.widgets(parent)#passing parent in order to be able to bind elements
		
