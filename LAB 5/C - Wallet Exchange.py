import sys

t = int(sys.stdin.readline())

while t > 0 :

    a,b = list(map(int, sys.stdin.readline().split()))

    if ( (a % 2) ^ (b%2) ) == 0 :
        print("Bob")
    else:
        print("Alice")

    t -= 1
