#Functions - organized code we can call later

def who_am_i(): #This is a function without parameters
	name = "Alfredo" #local variable
	age = 30
	print("My name is " + name + " and I am " + str(age) + " years old.")

who_am_i() #Calling function

def add_one_hundred(num):
	print(num + 100)
	
add_one_hundred(100)

def add(x,y):
	print(x + y)
	
add(7,7)

def multiply(x,y):
	return x * y #store
	
multiply (7,7)

print (multiply(7,7))

def square_root(x):
	print(x ** .5)

square_root(64)

def nl(): # new line
	print('\n')

nl()

#Thank you TCM Security