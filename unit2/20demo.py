# 20demo.py by Zucy

t = 1, 2, 3		# this is a tuple
print(t)
print(type(t))

stoopy = 'cats', 54, 380.95
print(stoopy)
print(type(stoopy))

# returns midpoint of a line on x,y coordinates
def midpoint(x1, y1, x2, y2):
	x = (x1 + x2) / 2
	y = (y1 + y2) / 2
	return x, y
	
print(midpoint(1, 2, 3, 4))		#calls midpoint fxn and send to print fxn
m = midpoint(1, 2, 3, 4)
mx, my = midpoint(1, 2, 3, 4)	#assigns variables to ea value in a tuple
print(mx)						#using assigned variable names
print(my)
print(m[0], m[1])				#using numeric index of tuples, starting at 0

i = 0       #ea time through the loop, value i increases by 1
while True:
       i = i + 1
       print('hello', i)      #any cammand, will run if true
       if i == 3: break    #break command stops the loop, in this case, when i reaches 3"
       
i = 0
while i < 3:
       i = i + 1
       print('hello', i)
       
for i in range (0, 5):
       print(i)

basket = 'milk', 'eggs', 'bread'
for thing in basket:		#this line defines "things"
	print(thing)

for i in range(len(basket)):
	print(basket[i])