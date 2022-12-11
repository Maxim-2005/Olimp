a, b = map(int, input().split())

if a + 1 < b and a + 1  > a and a != b:
	print(a + 1)
elif a - 1 > b and a - 1 < a and a != b:
	print(a - 1)
else:
	print(-1)
