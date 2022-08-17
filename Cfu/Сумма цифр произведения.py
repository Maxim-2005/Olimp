for i in range(int(input())):
	n, A = map(int, input().split())
	s = 0
	if len(str(A)) >= n - 1:
		s = sum(map(int, str(int('1' * n) * A)))
	else:
		s = sum(map(int, str(int('1' * len(str(A))) * A)))
		t = int('1' * (len(str(A)) + 2)) * A
		v = int(str(t)[len(str(t)) // 2])
		l = n - len(str(A))
		s += v * l
	print(s)
