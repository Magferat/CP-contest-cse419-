import sys
t = int(sys.stdin.readline())

while t > 0 :
    a,b,c = list(map(int, sys.stdin.readline().split()))


    if a == b :
        if c % 2 == 0 :
            print("Second")
        else:
            print("First")
    elif a > b :
        print("First")
    elif a < b :
        print("Second")

    t -= 1




