"""
					CSCI 503 - Assignment 5 - Spring 2019
					Progammer: Manoj Veluru
					Z-ID: Z1840907
					Section: 1
					Date Due: May 2, 2019
					Purpose: Geometric Shapes
"""

'''Importing Shape Abstract class and also math functions'''
from shape import Shape
from math import *

'''Class Rectangle derived from Shape Abstract class'''
class Rectangle(Shape):
	'''Constructor to create Rectangle with length and width'''
	def __init__(self,length=0,width=0):
		self.length = length
		self.width = width
	
	'''Overloading Append Operator iadd(+)'''
	def __iadd__(self,other):
		return Rectangle(self.length+other.length,self.width+other.width)
	
	'''Method to return area of Rectangle'''
	def area(self):
		return self.length*self.width
	
	'''Method to return Perimeter of Rectangle'''
	def perimeter(self):
		return 2*(self.length+self.width)
	
	'''To return dimensions of Geometric Shapes'''
	def __str__(self):
		if self.length==self.width and not self.length==0:
			return 'length = %.2f'%(self.length)
		else:
			return 'length = %.2f : width = %.2f'%(self.length,self.width)

'''Class Circle derived from Shape Abstract class'''		
class Circle(Shape):
	'''Constructor to create Circle with radius'''
	def __init__(self,radius=0):
		self.radius = radius
	
	'''Overloading Append Operator iadd(+)'''
	def __iadd__(self,other):
		return Circle(self.radius+other.radius)
	
	'''Method to return area of Circle'''
	def area(self):
		return pi*self.radius*self.radius
	
	'''Method to return Perimeter of Circle'''
	def perimeter(self):
		return 2*(self.radius*pi)
	
	'''To return dimensions of Geometric Shapes'''
	def __str__(self):
		return 'radius = %.2f'%(self.radius)

'''Class Triangle derived from Shape Abstract class'''
class Triangle(Shape):
	'''Constructor to create Triangle with 3 sides'''
	def __init__(self,a=0,b=0,c=0):
		self.a = a
		self.b = b
		self.c = c
	
	'''Overloading Append Operator iadd(+)'''
	def __iadd__(self,other):
		return Triangle(self.a+other.a,self.b+other.b,self.c+other.c)
	
	'''Method to return area of Triangle'''
	def area(self):
		k = (self.a+self.b+self.c)/2
		return sqrt(k*(k-self.a)*(k-self.b)*(k-self.c))
	
	'''Method to return Perimeter of Triangle'''
	def perimeter(self):
		return self.a+self.b+self.c
	
	'''To return dimensions of Geometric Shapes'''
	def __str__(self):
		if self.a==self.b==self.c and not self.a==0:
			return 'length = %.2f'%(self.a)
		else:
			return 'a = %.2f : b = %.2f : c = %.2f'%(self.a,self.b,self.c)

'''SubClass Square derived from Rectangle class'''		
class Square(Rectangle):
	'''Constructor to create Square with length'''
	def __init__(self,length=0):
		Rectangle.__init__(self,length,length)

'''SubClass rightTriangle derived from Triangle class'''
class rightTriangle(Triangle):
	'''Constructor to create rightTriangle with length and height'''
	def __init__(self,a=0,b=0):
		Triangle.__init__(self,a,b,sqrt(a*a+b*b))
	'''Overloading Append Operator iadd(+)'''
	def __iadd__(self,other):
		return rightTriangle(self.a+other.a,self.b+other.b)
	
	'''To return dimensions of Geometric Shapes'''
	def __str__(self):
		return 'length = %.2f : height = %.2f'%(self.a,self.b)

'''SubClass equTriangle derived from Triangle class'''		
class equTriangle(Triangle):
	'''Constructor to create equTriangle with side'''
	def __init__(self,side=0):
		Triangle.__init__(self,side,side,side)