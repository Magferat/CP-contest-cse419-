import sys

t = int(sys.stdin.readline())

while t > 0 :
    n,k = list(map(int, sys.stdin.readline().split()))

    arr = list(map(int, sys.stdin.readline().split()))
    arr.sort()
    s = 0
    i = 0
    while i < k-1 :
        if arr[i] == 1 :
            s += 1
        else:
            s += arr[i]*2 -1
        i += 1

    print(s)

    t-= 1




