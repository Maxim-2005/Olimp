arr = list(input().split())
arr.sort()

for i in range(317, 1000):
    q = i ** 2
    res = list(str(q))
    res.sort()
    if arr == res:
        print(q)
        break
