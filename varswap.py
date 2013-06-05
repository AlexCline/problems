def swap_with_var(a, b):
	print a,b
	c = None
	c = a
	a = b
	b = c
	print a,b

def swap_inplace(a, b):
	print a,b
	a, b = b, a
	print a,b

def swap_bitwise(a, b):
	print a,b
	a ^= b
	b ^= a 
	a ^= b
	print a,b

swap_with_var(3,4)
swap_inplace(5,6)
swap_bitwise(7,8)