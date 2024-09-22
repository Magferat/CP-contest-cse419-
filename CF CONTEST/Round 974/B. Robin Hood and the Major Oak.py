import sys

t =int(sys.stdin.readline())

while t > 0 :

    n,k = list(map(int, sys.stdin.readline().split()))
    if n == 1 :
        print("NO")
    else:
        r = n * n
        n -= 1
        a = 0

        while a < k and n > 0:
            r += n ** n

            a += 1
    t -= 1
