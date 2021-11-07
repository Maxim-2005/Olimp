N, M = map(int, input().split())

arr = []
arrMin = []
arrMinX = []
maxY = 0

for y in range(N):
    line = (list(map(int, input().split())))
    arr.append(line)
    minX = 100000000
    for x in range(M):
        if line[x] < minX:
            minX = line[x]
            posX = x
    arrMin.append(minX)
    arrMinX.append(posX)
    
for y in range(N):
    if arrMin[y] > maxY:
        maxY = arrMin[y]
        spX = arrMinX[y]
        spY = y

if maxY == 0:
    print(0)
else:
    print(maxY)
    print(spX, spY)
