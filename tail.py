def tail(file, num):
	assert num >= 0
	pos, lines = num+1, []

	while len(lines) <= num:
		try:
			f.seek(-pos, 2)
		except IOError:
			f.seek(0)
			break
		finally:
			lines = list(f)
		pos *=2
	return lines[-num:]

f = open('priodict.py', 'r')
print "".join(tail(f, 2))