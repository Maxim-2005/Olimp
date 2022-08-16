T = int(input())

for i in range(T):
	n, A = map(int, input().split())
	arr = [1] * n
	res = int(''.join(map(str, arr))) * A
	
	summ = 0
	for j in str(res):
		summ += int(j)
	print(summ)
