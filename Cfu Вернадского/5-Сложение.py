N = int(input())
arr1 = list(map(int, input().split()))
M = int(input())
arr2 = list(map(int, input().split()))
K = int(input())
temp = []
arr1.sort()
arr2.sort()

for i in range(min(len(arr1), K)):
	for j in range(min(len(arr2), K)):
		temp.append(arr1[i] + arr2[j])
temp.sort()
print(temp[K-1])
