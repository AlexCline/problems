from random import randrange

def quicksort(array):
	if len(array) <= 1:
		return array
	pivot = array.pop(randrange(len(array)))
	less = []
	more = []
	for x in array:
		if x <= pivot:
			less.append(x)
		else:
			more.append(x)
	return quicksort(less) + [pivot] + quicksort(more)


array = [2,5,3,1,8,7,4,6]
print quicksort(array)
