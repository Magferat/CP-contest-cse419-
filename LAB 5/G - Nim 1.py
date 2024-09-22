import sys

t = int(sys.stdin.readline())
c = 0
while t > 0 :
    c += 1
    n = int(sys.stdin.readline())
    white = list(map(int,sys.stdin.readline().split()))
    black = list(map(int,sys.stdin.readline().split()))
    total = 0
    for i in range(n):
        # print(black[i], white[i], black[i]^white[i])
             total ^= (black[i]-white[i] -1)
    # print(total, "t")

    if total == 0 :
        sys.stdout.write("Case "+str(c)+": black wins\n")
    else:
        sys.stdout.write("Case "+str(c)+": white wins\n")

    t -= 1
