import math

def binary(haystack, needle, min, max):
	if max < min:
		return None
	else:
		mid = (min + max) // 2
		if haystack[mid] > needle:
			return binary(haystack, needle, min, mid - 1)
		elif haystack[mid] < needle:
			return binary(haystack, needle, mid + 1, max)
		else:
			return mid

array = [1,1,2,3,5,8,13,21]
print array
print binary(array, 21, 0, len(array) - 1)
