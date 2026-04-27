#write a programto print Hello python
print("HEllo Dear user")
#addition
num1= float(input("Enter first number for addition: "))
num2= float(input("Enter second number for addition: "))
sum= num1 + num2
print("The sum of", num1, "and", num2, "is", sum)     
# Find the area of a triangle
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
area = 0.5 * base * height
print(f"The area of the triangle is: {area}")
# Swap two variables
a = input("Enter the first variable: ")
b = input("Enter the second variable: ")
print(f"Before swapping: a = {a}, b = {b}")
a, b = b, a
print(f"After swapping: a = {a}, b = {b}")