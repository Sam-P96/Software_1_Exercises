from math import pi
print("Give me the radius of a circle and I will tell you its area. ")
r = float(input("What is the radius of the circle? "))

A = pi * r**2

print("The area of a circle with a radius of {} units is {} unit^2".format(r, A))