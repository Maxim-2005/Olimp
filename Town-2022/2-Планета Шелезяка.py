arrA = input()
arrB = input()

arrA = list(set(arrA))
arrB = set(arrB)

t = []
arrA.sort()

for i in arrA:
	if i in arrB and i not in t:
		t.append(i)

if len(t) == 0:
	print("epidemic")
else:
	print(''.join(t))
		
