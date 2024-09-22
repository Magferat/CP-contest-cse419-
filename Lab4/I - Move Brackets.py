import sys

t = int(sys.stdin.readline())

while t > 0:

    n = int(sys.stdin.readline())

    g_str = sys.stdin.readline().strip()

    open = 0
    close = 0
    count = 0

    for i in g_str :

       if i == ")" :
           close += 1
           d = open - close
           if d < 0 :
               count += 1
               close -= 1
       else:
           open += 1
       # print(i, open-close, g_str)

    sys.stdout.write(str(count)+"\n")

    t -= 1

