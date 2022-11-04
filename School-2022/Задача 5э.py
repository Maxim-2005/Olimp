m, n = map(int, input().split())
arr = []

temp = 0

for i in range(m, n + 1):
	q = str(i ** 2)
	if q.endswith(str(i)) == True:
		arr.append(i);

print(*arr)
