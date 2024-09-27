import sys

t = int(sys.stdin.readline())


while t > 0 :

    n = int(sys.stdin.readline())
    planks = list(map(int, sys.stdin.readline().split()))

    if n <= 2 :
        sys.stdout.write("0\n")
    else :
        planks.sort()
        b1,b2 = planks[-1], planks[-2]
        planks.pop(-1)
        planks.pop(-1)
        # print(planks)
        k = 0

        for p in planks :
            if p >= 1 :
               # k += 1
               if k + 1 < b1 and k + 1 < b2 :
                    k += 1
        # print(k)
        sys.stdout.write(str(k)+"\n")

    t -= 1