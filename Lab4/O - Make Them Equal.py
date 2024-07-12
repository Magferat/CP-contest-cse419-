import sys

t = int(sys.stdin.readline())


while t > 0 :
    a, c = list(sys.stdin.readline().split())
    given =[x for x in sys.stdin.readlines()]

    n = int(a)
    word = n * [c]
    print(word, given)
    if word == given :
        print(0)
    else:
        x = 2
        while  x <= n :
            i = 1
            while i < n:
                if i % x != 0 :
                    print(i, x)
                    given[i-1] = c

                    if given == word:
                        sys.stdout.write(str(x))
                        sys.stdout.write("\n")
                        x = n + 5
                        break

                i += 1

            x+= 1


    # if len(n) != len(k) :
    #     sys.stdout.write(str(False))
    #     sys.stdout.write("\n")
    # elif len(n) == len(k) == 1 and n != k:
    #     sys.stdout.write(str(False))
    #     sys.stdout.write('\n')
    # else:
    #
    #     for i in n :
    #         if i not in k:
    #             sys.stdout.write(str(False))
    #             sys.stdout.write('\n')
    #             break
    #     sys.stdout.write(str(True))
    #     sys.stdout.write('\n')




    t -= 1

