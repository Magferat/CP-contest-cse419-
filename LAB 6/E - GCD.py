import math
import sys

num = -1

while num != 0 :
    num = int(sys.stdin.readline())
    if num != 0 :
        g = num - 1

        for i in range(2,num) :
            for j in range(i+1, num+1):
                # print(i,j)
                g += math.gcd(i,j)
        sys.stdout.write(str(g)+"\n")

# 10
# 100
# 500
# 0
