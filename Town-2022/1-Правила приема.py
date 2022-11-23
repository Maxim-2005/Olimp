a, b, c = map(int, input().split())
a1, b1, c1 = map(int, input().split())

if a > a1 and b > b1 or b > b1 and c > c1 or a > a1 and c > c1:
	print(1)
elif a < a1 and b < b1 or b < b1 and c < c1 or a < a1 and c < c1:
	print(2)
else:
	print(0)
