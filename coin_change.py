def coin_change(nums, target, partial):
	s = sum(partial)

	if s == target:
		print "sum(%s)=%s"%(partial,target)
	if s >= target:
		return

	for i in range(len(nums)):
		n = nums[i]
		remaining = nums[i+1:]
		sum_ints(remaining, target, partial + [n])

coin_change(range(0,15), 25, list())