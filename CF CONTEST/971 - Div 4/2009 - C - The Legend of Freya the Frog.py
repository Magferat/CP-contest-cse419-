import sys

t = int(sys.stdin.readline())

while t > 0 :

    x,y,k = list(map(int, sys.stdin.readline().split()))

    i,j = 0,0

    jump = 0
    state = 'x'
    while i <= x or j <= y:
        if state == 'x' and i < x:
            jump += 1
            i += k
            print(state, "u")
            if j >= y and i < x :
                state = 'x'
            else:
                state = 'y'

        elif state == 'y' and j < y:
            jump += 1
            j += k
            print(state,"d")
            if i >= x and j < y :
                state = 'y'
            else:

                state = 'x'


    print(jump)

    t -= 1
