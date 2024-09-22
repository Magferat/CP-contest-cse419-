import sys

t = int(sys.stdin.readline())
c = 0
while t > 0 :
    c += 1
    n = int(sys.stdin.readline())
    position = list(map(int,sys.stdin.readline().split()))
    total = 0
    i = 1
    while i < n * 2:
        # print(position[i], position[i-1])
        total ^= position[i] - position[i-1] - 1
        i += 2

    # print(total)


    if total != 0:
        sys.stdout.write("Case "+str(c)+": Alice\n")
    else:
        sys.stdout.write("Case "+str(c)+": Bob\n")

    t -= 1
