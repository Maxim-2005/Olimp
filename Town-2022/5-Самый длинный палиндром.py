S = '-' + '-'.join(input()) + '-'
peak = 1
d = len(S)

for i in range(len(S)):
	temp =  -1
	for j in range(min(i, d - i - 1) + 1):
		if S[i - j] == S[i + j]:
			temp += 1
			peak = max(peak, temp)
		else:
			break
print(peak)



#S = input()
#peak = 0
#
#for i in range(len(S)):
#	for j in range(i, len(S)):
#		test =  S[i:j+1]
#		if test == test[::-1]:
#			peak = max(peak, len(test))
#			
#print(peak)
