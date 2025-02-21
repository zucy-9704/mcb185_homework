# triangularnumber.py by Zucy

# a triangular number is like a factorial but addition

def trinumb(n):	#define function
	i = 0	# i is the value that 'holds' the sum, this value is increasing as you add numbers
	for int in range(n+1):	# defining a new variable 'int' 
		# int = 0, 1, 2, ...
		i = i + int	# modifying value i
	return i	# returns final modified version i
	
print(trinumb(3))