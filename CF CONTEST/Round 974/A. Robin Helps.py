import sys

t =int(sys.stdin.readline())

while t > 0 :

    n,k = list(map(int, sys.stdin.readline().split()))
    gold = list(map(int, sys.stdin.readline().split()))
    robin = 0
    poor = 0
    for g in gold :
       if g >= k :
           robin += g
       if g == 0 :
           if robin > 0 :
               robin -= 1
               poor += 1

    sys.stdout.write(str(poor)+"\n")



    t -= 1