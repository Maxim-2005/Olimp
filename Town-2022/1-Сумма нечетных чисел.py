for i in range(int(input())):
	L, R = map(int, input().split())
	print(((R + R % 2) ** 2 - ((L- L % 2) ** 2))  // 4)

#T = int(input())
#S = 0
#
#for i in range(T):
#	L, R = map(int, input().split())
#	for j in range(L, R+1):
#		if j % 2 > 0:
#			S += j
#	print(S)
#	S = 0
