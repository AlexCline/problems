def genrange(lo, hi, exclude):
	result = range(lo, hi)
	for num in reversed(sorted(exclude)):
		if (num - lo) < len(result):
			result.pop(num - lo)

	return result

print genrange(0, 10, [6,8,11])