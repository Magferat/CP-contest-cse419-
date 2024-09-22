import sys

t = int(sys.stdin.readline())

while t > 0 :
    length, jump, freez= list(map(int, sys.stdin.readline().split()))
    seq = sys.stdin.readline()

    if jump == length :
        print("YES")
    else :
        i = 0
        r = True

        while i < length :

            current = seq[i]

            if current == "L" and jump > 0:
                i += jump
            elif current == "W" :
                if freez > 0 :
                    i += 1
                    freez -= 1
                else:
                    r = False
                    break
            elif current == "C" :
                if i == 0 :
                    i += jump
                else :
                    r = False
                    break
        if r :
            print("YES")
        else:
            print("NO")








    t-= 1




