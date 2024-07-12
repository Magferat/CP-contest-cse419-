import sys

t = int(sys.stdin.readline())


while t > 0 :
    n, k = list(sys.stdin.readline().split())

    if len(n) != len(k) :
        sys.stdout.write(str(False))
        sys.stdout.write("\n")
    elif len(n) == len(k) == 1 and n != k:
        sys.stdout.write(str(False))
        sys.stdout.write('\n')
    else:

        for i in n :
            if i not in k:
                sys.stdout.write(str(False))
                sys.stdout.write('\n')
                break
        sys.stdout.write(str(True))
        sys.stdout.write('\n')




    t -= 1

