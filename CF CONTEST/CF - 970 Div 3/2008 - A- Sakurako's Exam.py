import sys

t = int(sys.stdin.readline().strip())

while t > 0 :

    a,b = list(map(int, sys.stdin.readline().strip().split()))

    if a % 2 == 0 and b % 2 == 0 :
        sys.stdout.write("YES \n")
    elif a % 2 != 0 or b % 2 != 0 :
        if a % 2 != 0 and a>= 2:
            a -= 2
            b -= 1
            if a % 2 == 0 and b % 2 == 0 :
                sys.stdout.write("YES \n")
            else:
                sys.stdout.write("NO\n")



    t-=1