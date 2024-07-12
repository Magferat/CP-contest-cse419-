import sys

t = int(sys.stdin.readline())


while t > 0 :

    n, k = list(map(int, sys.stdin.readline().split()))

    a_arr = list(map(int, sys.stdin.readline().split()))
    b_arr = list(map(int, sys.stdin.readline().split()))

    a_arr.sort()
    b_arr.sort()

    if k == 0 :
        print(sum(a_arr))

