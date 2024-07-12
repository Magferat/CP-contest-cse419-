# your code goes here

import sys

t = int(sys.stdin.readline().strip())

while t > 0:

    n = int(sys.stdin.readline().strip())
    arr = list(map(int, sys.stdin.readline().split()))
    max_ = max(arr)
    sum = 0
    if max_ < 0 :
        sys.stdout.write(str(max_)+" "+str(n)+"\n")
    else:
        for i in range(n):
            sum += arr[i]
            if max_ < sum :
                max_ = sum
        sys.stdout.write(str(sum) + " " + str(n) + "\n")


    t -= 1