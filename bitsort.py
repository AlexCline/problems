def bitsort(input):
	l, u = 0, (len(input) - 1)
	while(l < u):
		if input[l] == 1:
			if input[u] == 0:
				input[l] ^= 1
				input[u] ^= 1
				l += 1
			u -= 1
		else:
			l += 1

	return input

print bitsort([0,1,1,0,1,0,1,0,0,1,1,1,0])