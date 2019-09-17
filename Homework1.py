import math
name = input("What is your name: ")
print("Hello " + name)

number1 = int(input("write the first number: "))
number2 = int(input("write the second number: "))
print("The division of both numbers is: "+str(math.ceil(number1/number2)))

radius = int(input("Please enter radius of a circle: "))
print("The surface area of the circle is: "+str(radius**2*math.pi))