import sys

t = int(sys.stdin.readline().strip())

while t > 0 :
    length = int(sys.stdin.readline().strip())

    array = list(map(int, sys.stdin.readline().strip().split()))

    if length > 1 :
        type_p = {0:0, 1:0}

        for i in range(length):

            if array[i] % 2 != i % 2 :
                type_p[array[i] % 2] += 1

        if type_p[0] == type_p[1]:
            sys.stdout.write(str(type_p[0]) + "\n")
        else:
            sys.stdout.write("-1 \n")
    else:
        if array[0] % 2 == 0 :
            sys.stdout.write("0 \n")
        else:
            sys.stdout.write("-1 \n")
    t -= 1