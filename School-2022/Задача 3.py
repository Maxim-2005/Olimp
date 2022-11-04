print("Введите число сказок > 7")
N = int(input())
S = 0

while N > 0:
	if N % 3 > 0:
		N -= 5
		S += 1
	else:
		S = S + N // 3
		break
		
print(S)
