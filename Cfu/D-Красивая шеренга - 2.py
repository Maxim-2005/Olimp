N = int(input())
maxCount = 0
count = 0
prev = 0

for i in map(int, input().split()):
	if i > prev:
		count = 1
	else:
		count += 1
	if maxCount < count:
		maxCount = count
	prev = i
print(maxCount)
