import sys

t = int(sys.stdin.readline())


while t > 0:
    n, k = list(map(int, sys.stdin.readline().split()))
    arr =[x for x in sys.stdin.readlines()]

    i,j = 0, n-1

    while i < j :

        sum = arr[i] + arr[j]

        if sum == k :
            sys.stdout.write(str(i+j))
            # sys.stdout.write(j)
            # sys.stdout.write("\n")




    t -= 1