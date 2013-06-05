def addone(arr, index):
	if index == None:
		index = len(arr) - 1
	if arr[index] + 1 > 9 :
		arr[index] = 0
		if index - 1 < 0:
			arr.insert(0, 1)
		else:
			addone(arr, index - 1)
	else:
		arr[index] += 1

	return arr

	# arr.reverse()
	# if(arr[index] + 1 > 9):
	# 	arr[index] = 0
	# 	arr.reverse()
	# 	if index + 1 > len(arr) - 1:
	# 		arr.insert(0, 1)
	# 	else:
	# 		addone(arr, index + 1)
	# else:
	# 	arr[index] += 1
	# arr.reverse()
	# return arr

print addone([1,0,0], None)
print addone([9,9], None)