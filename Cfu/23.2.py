N = int(input())
arr = list(map(int, input().split()))
K = int(input())
h = 0

for i in arr:
    if i < 0:
        h += 1
if h <= K:
    print(h)
else:
    print(h)
    print(abs(min(arr)))
