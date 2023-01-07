N = int(input())
arr = list(map(int, input().split()))
l = m = sum(arr)
r = 0
for i in arr:
	l -= i
	r += i
	m = min(m, abs(r - l));
print(m)
