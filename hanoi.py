def hanoi(size, source, helper, target):
        if size > 0:
		hanoi(size - 1, source, target, helper)
		if source:
			print source, helper, target
			target.append(source.pop())
		hanoi(size - 1, helper, source, target)


source = [4,3,2,1]
target = []
helper = []
hanoi(len(source), source, helper, target)

print source, helper, target
