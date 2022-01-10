N = int(input())
P = 0
arr1 = []
arr2 = []

for i in range(N):
    a, b = input().split()
    if b == '>':
        arr1.append(int(a))
    else:
        arr2.append(int(a))

print(min(arr1) - max(arr2))
