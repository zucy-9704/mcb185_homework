# factorial.py	by Zucy

def factorial(n):	# this does not account for factorial of 0
	i = 1
	for int in range(1, n+1):
		i = i * int
	return i
		
print(factorial(4))