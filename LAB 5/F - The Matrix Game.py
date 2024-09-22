import sys

t = int(sys.stdin.readline())

while t > 0 :
    a_input = sys.stdin.readline()
    if a_input != '\n' :
        n, m = list(map(int, a_input.split()))
        # print(n,m)
        a = []
        r = n
        while r > 0 :
            b_input = sys.stdin.readline()
            if b_input != '\n':
                x = b_input.split()
                a.append(x)
                r -= 1

        total = n * m

        # print(total, n, m)
        if total % 2 == 0 :
            print("SECOND")
        else:
            print("FIRST")
        t -= 1




