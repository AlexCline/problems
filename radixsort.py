def radixsort(array):
	size = len(array)
	bsize = 10
	div = 1

	while True:
		buckets = [list() for _ in range(bsize)]

		for value in array:
			low = value % bsize
			low /= div
			buckets[low].append(value)
		bsize = bsize * 10
		div = div * 10

		if len(buckets[0]) == size:
			return buckets[0]

		array = []
		new_array = array.append
		for x in buckets:
			for y in x:
				new_array(y)

print radixsort([18,5,100,3,1,19,6,0,7,4,2])