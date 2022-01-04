t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    k = n * m
    s = int((1 + k) * k / 2)
    ps = s / 2
    v = m // 2
    
    col1 = int((1 + (n - 1) * m + 1) * n / 2)
    colV = int((v + (n - 1) * m + v) * n / 2)
    colV2 = int(((v + 1) + (n - 1) * m + (v + 1)) * n / 2)
    
    vs =  int((col1 + colV) * v / 2)
    vs2 =  int((col1 + colV2) * (v + 1) / 2)

    vr = abs(ps - vs)
    vr2 = abs(ps - vs2)

    if vr <= vr2:
        minV = vr
        col = v
    else:
        minV = vr2
        col = v + 1
    
    h = round(n * 0.7066667) #PEREDELAT'
    
    hs = int((1 + h * m)  * h * m / 2)
    hs2 = int((1 + ((h + 1) * m))  * ((h + 1) * m) / 2)

    hr = abs(ps - hs)
    hr2 = abs(ps - hs2)
    
    if hr <= hr2:
        minH = hr
        row = h
    else:
        minH = hr2
        row = h + 1

    if minV < minH:
        print("V", v+2)
    else:
        print("H", h+1)
