S, A, B = map(float, input().split())

if S % A == S % B:
    print(0)
elif S % A > S % B:
    print(2)
else:
    print(1)
