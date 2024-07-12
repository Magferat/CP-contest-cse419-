import sys

t = int(sys.stdin.readline())

while t > 0 :
    n,m,k= list(map(int, sys.stdin.readline().split()))

    a = []
    while n > 0 :
        a.append(str(n))
        n -= 1

    print(' '.join(a))

    t-= 1




