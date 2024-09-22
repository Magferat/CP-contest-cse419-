import sys

t = int(sys.stdin.readline())

while t > 0 :

    n = int(sys.stdin.readline())
    circle = sys.stdin.readline()

    up = 0

    for coin in circle :
        if coin == "U" :
            up += 1

    if up % 2 == 0 :
        sys.stdout.write("NO\n")
    else:
        sys.stdout.write("YES\n")

    t -= 1
