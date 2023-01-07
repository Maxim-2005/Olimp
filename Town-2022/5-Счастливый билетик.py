N = input()
miniL = maxiL = miniR = maxiR = 0

for i in range(3):
	if N[i] == "*":
		maxiL += 9
	else:
		miniL += int(N[i])
		maxiL += int(N[i])
	if N[i+3] == "*":
		maxiR += 9
	else:
		miniR += int(N[i+3])
		maxiR += int(N[i+3])

if  maxiL < miniR or maxiR < miniL:
	print("No")
else:
	print("Yes")
