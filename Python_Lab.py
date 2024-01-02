"""
02/0/2024
AWS re/Start : Python Day 1 week 5
"""
print("Hello, World")
print("Python has three numeric types: int, float, and complex")
print("\n")
#################################################

myValue=1
print(myValue)
print(type(myValue))
print(str(myValue) +  " is of the data type" + str(type(myValue)))
print("\n")
#####################################################

myValue=3.14
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))
print("\n")
#######################################################

myValue=5j
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))
print("\n")

#######################################################

myValue=False
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))
print("\n")

########################################################

myString = "This is a string."
print(myString)
print(type(myString))
print(myString + " is of the data type " + str(type(myString)))

############################################################

firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

#########################################################

name = input("What is your name? ")
#print(name)

##########################################################
color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")

print("{}, you like a {} {}!".format(name,color,animal))