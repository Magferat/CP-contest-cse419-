import sys

t = int(sys.stdin.readline())

while t > 0 :
    a,b,n = map(int, sys.stdin.readline().split())
    tools = list(map(int, sys.stdin.readline().split()))
    tools.sort()

    c = b
    i = 0
    for x in tools:

        c += min(a-1,x)

    sys.stdout.write(str(c)+"\n")


    t -= 1

