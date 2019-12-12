#This program is the second lab test that is a 3D vector using classes to allow for multiplication, addition, subtraction, dot point and a few other functions
#in this code
#Author: Robert Hatfield
#Student Number: c18475892
#Date: 12/12/19
#Compiler: PYcharm

import math # For this import I used it later in the magnitude section to get the square root

class vector3D: # This is the main class with all of the calculations
    def __init__(self,x,y,z):
        self.x=float(x)
        self.y=float(y)
        self.z=float(z)

    def __add__(self, v2):# This is the addition for the vectors which can be seen by running examples in main
        return vector3D(self.x+v2.x,self.y+v2.y, self.z+v2.z)

    def __sub__(self, v2):# This is the subtraction for the vectors which can be seen running examples in main
        return vector3D(self.x-v2.x,self.y-v2.y,self.z-v2.z)

    def __mul__(self, v2):# This is the multiplication for the vectors or for the integer and it can be seen by running examples in main
        if (type(self)==type(v2)):# This if statement is used to check if it is an integer or another vector that is being multiplied

            return self.x*v2.x+self.y*v2.y+self.z*v2.z

        else:

            return vector3D(self.x*v2,self.y*v2,self.z*v2)


    def __str__(self):# This str function is used to display the results properly when printing
        return "({} {} {})".format(self.x,self.y,self.z)

    def magnitude(self):# This is the magnitude function that uses the math import to get the square root after multiplying the vectors by the power of 2
        ans = self.x*self.x+self.y*self.y+self.z*self.z
        ans = float(ans)
        return math.sqrt(ans)

#main
v1 = vector3D(1,2,3)
v2 = vector3D(5,5,5)

print("Printing v1")
print("v1 = ", v1)
print("\n")

print("Printing v2")
print("v2 = ",v2)
print("\n")

v3 = v1 + v2
print("Printing addition")# addition
print("v1 + v2 = ", v3)
print("\n")

v4 = v1 - v2
print("Printing subtraction")# subtraction
print("v1 - v2 = ", v4)
print("\n")

print("Printing dot product")# dot product
v5 = v1 * v2
print("v1 * v2 = ", v5)
print("\n")

print("Printing integer multiplication")# integer multiplication
v6 = v1 * 2
print("v1 * 2.5 = ", v6)
print("\n")

print("v1 magnitude is ", v1.magnitude())# magnitude function

print("\n")
print("Thank you for using this code!!")
print("This program will now end")# exit message