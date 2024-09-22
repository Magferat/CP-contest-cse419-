import sys

t = int(sys.stdin.readline())

while t > 0 :

    a,b = list(map(int, sys.stdin.readline().split()))

    sys.stdout.write(str(b-a)+"\n")

    t -= 1
