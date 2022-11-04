print("Введите число не првевышающее 20")
N = int(input())
arr = list(map(int, input().split()))

temp = 0

for i in range(1, N+1):
	if arr[i - 1] > i:
		temp += arr[i - 1]
	
print(temp)
