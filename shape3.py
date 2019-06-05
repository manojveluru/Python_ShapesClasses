"""
					CSCI 503 - Assignment 5 - Spring 2019
					Progammer: Manoj Veluru
					Z-ID: Z1840907
					Section: 1
					Date Due: May 2, 2019
					Purpose: Geometric Shapes
"""
from shape2 import *

'''SubClass Box derived from Rectangle class'''
class Box(Rectangle):
	'''Constructor to create Box with length and width and height'''
	def __init__(self,length=0,width=0,height=0):
		Rectangle.__init__(self,length,width)
		self.height = height
	
	'''Overloading Append Operator iadd(+)'''
	def __iadd__(self,other):
		return Box(self.length+other.length,self.width+other.width,self.height+other.height)
	
	'''Method to return area of Box'''
	def area(self):
		return 2*Rectangle.area(self)+self.height*Rectangle.perimeter(self)
	
	'''Method to return Volume of Box'''
	def volume(self):
		return self.height*Rectangle.area(self)
	
	'''To return dimensions of Geometric Shapes'''
	def __str__(self):
		return 'length = %.2f : width = %.2f : height = %.2f'%(self.length,self.width,self.height)

'''SubClass Cube derived from Square class'''		
class Cube(Square):
	'''Constructor to create Cube with height'''
	def __init__(self,height=0):
		Square.__init__(self,height)
		self.height = height
	
	'''Overloading Append Operator iadd(+)'''
	def __iadd__(self,other):
		return Cube(self.height+other.height)
	
	'''Method to return area of Cube'''
	def area(self):
		return 6*Square.area(self)
	
	'''Method to return Volume of Cube'''
	def volume(self):
		return self.height*Square.area(self)

'''SubClass Cylinder derived from Circle class'''	
class Cylinder(Circle):
	'''Constructor to create Cylinder with radius and height'''
	def __init__(self,radius=0,height=0):
		Circle.__init__(self,radius)
		self.height = height
	
	'''Overloading Append Operator iadd(+)'''
	def __iadd__(self,other):
		return Cylinder(self.radius+other.radius,self.height+other.height)
	
	'''Method to return area of Cylinder'''
	def area(self):
		A1 = self.height*Circle.perimeter(self)
		return 2*Circle.area(self)+A1
	
	'''Method to return Volume of Cylinder'''
	def volume(self):
		return self.height*Circle.area(self)
	
	'''To return dimensions of Geometric Shapes'''
	def __str__(self):
		return 'radius = %.2f : height = %.2f'%(self.radius,self.height)

'''SubClass Cone derived from Circle class'''
class Cone(Circle):
	'''Constructor to create Cone with radius and height'''
	def __init__(self,radius=0,height=0):
		Circle.__init__(self,radius)
		self.height = height
	
	'''Overloading Append Operator iadd(+)'''
	def __iadd__(self,other):
		return Cone(self.radius+other.radius,self.height+other.height)
	
	'''Method to return area of Cone'''
	def area(self):
		s = sqrt(self.radius*self.radius+self.height*self.height)
		A1 = 0.5*s*Circle.perimeter(self)
		return Circle.area(self)+A1
	
	'''Method to return Volume of Cone'''
	def volume(self):
		return (1/3)*self.height*Circle.area(self)
	
	'''To return dimensions of Geometric Shapes'''
	def __str__(self):
		return 'radius = %.2f : height = %.2f'%(self.radius,self.height)

'''SubClass Sphere derived from Circle class'''
class Sphere(Circle):
	'''Constructor to create Sphere with radius'''
	def __init__(self,radius=0):
		Circle.__init__(self,radius)
	
	'''Overloading Append Operator iadd(+)'''
	def __iadd__(self,other):
		return Sphere(self.radius+other.radius)
	
	'''Method to return area of Sphere'''
	def area(self):
		return 4*Circle.area(self)
	
	'''Method to return Volume of Sphere'''
	def volume(self):
		return (4/3)*self.radius*Circle.area(self)

'''SubClass Tetrahedron derived from equTriangle class'''
class Tetrahedron(equTriangle):
	'''Constructor to create Tetrahedron with side'''
	def __init__(self,a=0):
		equTriangle.__init__(self,a)
	
	'''Overloading Append Operator iadd(+)'''
	def __iadd__(self,other):
		return Tetrahedron(self.a+other.a)
	
	'''Method to return area of Tetrahedron'''
	def area(self):
		return 4*equTriangle.area(self)
	
	'''Method to return Volume of Tetrahedron'''
	def volume(self):
		h = sqrt((2/3))*(self.a)
		return (1/3)*h*equTriangle.area(self)
	
	'''To return dimensions of Geometric Shapes'''
	def __str__(self):
		return 'length = %.2f'%(self.a)
