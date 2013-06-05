#def most_common(obj):
#	return max(set(obj), key=obj.count)
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
			less.append(x)

	return quicksort(less) + [pivot] + quicksort(more)

def most_common(obj):
	currunlen = 0
	maxrunlen = 0
	currun = 0
	maxrun = 0
	last_item = None

	for item in quicksort(obj):
		# if prev item is not the same as the current item
		if last_item is None or last_item != item:
			# if we just found a new long run, 
			if currunlen > maxrunlen:
				maxrunlen = currunlen
				maxrun = currun
			# otherwise, reset current run to this item
			currunlen = 1
			currun = item
			last_item = item
		else:
			# we found another item, add one to the run len
			currunlen += 1

	return maxrun

arry = range(0,25) + [10,11,10,12,10]
print most_common(arry)