# 50demo.py	by Zucy

# sets
s = {'A', 'C', 'G'}
print(s)
s.add('T')
print(s)
s.add('A')	# adding duplicates doesn't do anything
print(s)
	# bc there is no order, there are no indices
	
# dictionaries
	# like list, but indices are strings (not numbers)
	# dict['hey']: 'hey' is a string index
	# no append() for dictionaries
	# generate by
		# d = {}
		# d = dict()
d = {'dog': 'woof', 'cat': 'meow'}
	# dictionaries have key:value pairs
	# index for key returns value
print(d)
print(d['dog'])
# to add new key:value pair...
d['pig'] = 'oink'
print(d)
# to chance key's value...
d['cat'] = 'mew'
print(d)
# to delete an item...
del d['pig']
print(d)
# to check if key exists, use in (like you would in list or set)
if 'dog' in d: print(d['dog'])

# iterate through dictionary
for key in d:
	print(f'{key} says {d[key]}')
		# f is necessary to associate key:value with loop

for k, v in d.items(): print(k, 'says', v)
	# dict.items() necessary to separate the variables
	
# separate only keys or only values
print(d.keys(), d.values(), list(d.values()))

# can count using a dictionary
"""
count = {}
for nt in seq:
	if nt not in count: count[nt] = 0
	count[nt] += 1
"""











