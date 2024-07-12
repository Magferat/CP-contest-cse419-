t = int(input().strip())

while t > 0:
    n,a,b = [int(i) for i in input().split()]

    if n == a == b :
        print('Yes')
    elif a + b + 2 <= n :
        print('Yes')
    else:
        print('No')
    t -= 1