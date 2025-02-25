def midpoint(x1, y1, x2, y2):
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    return x, y
    
print(midpoint(1, 2, 3, 4))
m = midpoint(1, 2, 3, 4)	#creating a tuple
mx, my = midpoint(1, 2, 3, 4)	# unpacking the tuple and assigning new variable names
print(mx, my)
print(mx)
print(m)