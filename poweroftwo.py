def poweroftwo(num):
	return (num & (num - 1)) == 0

print poweroftwo(8)
print poweroftwo(7)

8 = 1 0 0 0
7 = 0 1 1 1
-----------
& = 0 0 0 0