import sys

t = int(sys.stdin.readline())

while t > 0 :

    n = int(sys.stdin.readline())

    seq = sys.stdin.readline()



    if n == 2 :
        sys.stdout.write(str(1) +"\n")

    else:
        open = 0
        close = 0
        i = 0
        while i < n:

            s = seq[i]
            if s == "(":
                if seq[i+1] == ")" :
                    temp = i
                    i += 1
                else:
                    open += 1
            elif s == ")":
                if open > close :
                    open -= 1
                else :
                    close += 1
            i += 1

        sys.stdout.write(str(close) + "\n")

    t -= 1