x1, y1, x2, y2 = map(int, input().split())
a = (y1 - y2) / (x1 - x2);
b = y2 - a * x2;
print(b)
