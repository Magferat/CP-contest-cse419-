import sys

t = int(sys.stdin.readline())


while t > 0 :
    n, k = list(sys.stdin.readline().split())

    if len(n) != len(k) :
        sys.stdout.write("False\n")

    elif len(n) == len(k) == 1 and n != k:
        sys.stdout.write("False\n")

    else:

        n_ascii = []
        k_ascii = []

        for i in range(len(n)) :
            n_ascii.append(ascii(n[i]))
            k_ascii.append(ascii(k[i]))

        n_ascii.sort()
        k_ascii.sort()
        if n_ascii == k_ascii :
            sys.stdout.write("True\n")
        else:
            sys.stdout.write("False\n")

    t -= 1

