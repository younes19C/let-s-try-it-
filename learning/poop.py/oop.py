# this file is about oop
#in python
# class is a blueprint for creating objects
#attributes =is/has (ex;name,hieght,age)
#methods = does (ex;eat,sleep,run)
#class is a blueprint for creating objects (class=attributes+methods)
#to define a class we use class followed by the name of the class that start with(majiscule)
#to define a method we use def followed by the name of the method that start with (lowercase)
#to define an attribute we use the name of the attribute that start with (lowercase)
import math 
class Car :
    make= None
    color=None
    model=None
    year= None
    def __init__(self,make,color,model,year):
        self.make=make
        self.color=color
        self.model=model
        self.year=year
    def drive(self):
        print("this car is driving")
    def stop(self):
        print("this car is stopping")


 # class point 
class Point :
    def __init__(self,coordx,coordy) :
        self.x=coordx
        self.y=coordy
    #D´efinition de la m´ethode distance
    def distance(self,pt) :
        dist=math.sqrt((self.x-pt.x)**2+(self.y-pt.y)**2)
        return dist
    #D´efinition de la m´ethode affichePoint()
    def affichePoint(self) :
        print("Point(",self.x,",",self.y,")")
    
