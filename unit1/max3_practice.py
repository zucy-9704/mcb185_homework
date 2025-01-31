# max3_practice by Zucy

def max3(x, y, z): 
	if x > y > z: return x
	elif y > z > x: return y
	elif z > x > y: return z
	elif z > y > x: return z
	elif x > z > y: return x
	elif y > x > z: return y
	else: return
	
print(max3(3, 5, 7))
