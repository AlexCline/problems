def selection(array):
	for index in range(0, len(array)):
		min = index
		for i in range(index, len(array)):
			if array[min] > array[i]:
				min = i
		array[index], array[min] = array[min], array[index]
	return array


array = [13,2,5,1,21,8,3,1]
print selection(array)
