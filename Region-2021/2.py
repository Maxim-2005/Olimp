t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    k = n * m
    s = int((1 + k) * k / 2) ; print('VSYA SYMMA', s)  
    ps = s / 2 ; print('IDEAILNOE RAZDELENIE', ps)
    v = m // 2
    col1 = int((1 + (n - 1) * m + 1) * n / 2) ; print('SYMMA PERVOI KOLONKI', col1)  
    colV = int((v + (n - 1) * m + v) * n / 2); print('SYMMA SREDNEI KOLINKI', colV)
    vs =  int(col1 + colV) * v / 2 ; print('SYMMA LEVOI KOLONKI', vs)
    vr = ps - vs; print('OTKLONENIE LEVOI KOLONKI', vr)
    vs2 =  s - vs ; print('SYMMA PRAVOI KOLONKI', vs2)
    vr2 = ps - vs2; print('OTKLONENIE PRAVOI KOLONKI', vr2)
