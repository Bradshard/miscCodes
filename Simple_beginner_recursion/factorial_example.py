import math
def factorial(n):
	global a
	if (n == 0):
		return 1
	elif (n == 1):
		return 1
	else :
		while (n >= 2):
			a += n*factorial(n-1)
			n = n - 1 
			return a
def positive_check(p):
	if (p >= 0):
		return factorial(p)
	else:
		print("Please give me a positive number")
		return number()
def number(b):
	b = int(input("give me a number: "))
	return positive_check(b)
a = 0
b = None
print(number(b))