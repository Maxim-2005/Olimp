N, M = map(int, input().split())
X, Y = map(int, input().split())
X-=1
Y-=1
K = int(input())
arr=[[[] for j in range(M)] for i in range(N)]
res='SUCCESS'
for i in range(K):
	a, b, c = input().split()
	a, b = int(a)-1, int(b)-1
	if c not in arr[a][b]:
		arr[a][b].append(c)
	if c == 'U' and a - 1 >= 0:
		a -= 1
		c = 'D'
	elif c == 'L' and b - 1 >= 0:
		b -= 1
		c = 'R'
	elif c == 'R' and b + 1 < M:
		b += 1
		c = 'L'
	elif c == 'D' and a +1 < N:
		a += 1
		c = 'U'
	if c not in arr[a][b]:
		arr[a][b].append(c)
for i in input():
	for j in arr[X][Y]:
		if i == j:
			res = 'FAIL'
			break
	if res=='FAIL':
		break
	if i == 'U':
		X -= 1
	elif i == 'L':
		Y -= 1
	elif i == 'R':
		Y += 1
	elif i == 'D':
		X += 1
    if X<0 or X>=N or Y<0 or Y>=M:
		res = 'FAIL'
		break
print(res)
