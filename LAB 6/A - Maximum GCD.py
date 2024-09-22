import math
import sys

t = int(sys.stdin.readline())

while t > 0 :

    arr = list(map(int,sys.stdin.readline().split()))
    max = 1
    # print(arr)
    for i in range(len(arr)):

        for j in range(i+1, len(arr)):
            gcd = math.gcd(arr[i], arr[j])
            if gcd > max :
                max = gcd
    print(max)

    t -= 1

