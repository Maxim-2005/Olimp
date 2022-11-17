S = '-' + '-'.join(input()) + '-'
d = len(S)
arr = [0] * d
peak = c = r = 0

for i in range(d):
	j = 0 if i > c + r  else min(arr[c-(i-c)], c + r - i)
	while i - j > 0 and i + j < d - 1 and S[i - j - 1] == S[i + j + 1]:
		j += 1
	if i + j > c + r:
		c, r = i, j
	arr[i] = j
	peak = max(peak, j)
print(peak)

#S = '-' + '-'.join(input()) + '-'
#peak = 1
#d = len(S)
#
#for i in range(len(S)):
#	temp =  -1
#	for j in range(min(i, d - i - 1) + 1):
#		if S[i - j] == S[i + j]:
#			temp += 1
#			peak = max(peak, temp)
#		else:
#			break
#print(peak)

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
