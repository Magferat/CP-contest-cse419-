import sys

t = int(sys.stdin.readline())

while t > 0 :
    n,c = sys.stdin.readline().strip().split()
    n = int(n)
    word = sys.stdin.readline().strip()
    # print(n*c==word)
    if n*c == word :
        sys.stdout.write("0\n")
    else:
        print(word)
        not_c = []

        for w in range(n) :
            if word[w] != c :
                not_c.append(w+1)
        print(not_c)
        x = 2
        one = True
        while x <= n :
            for i in not_c:
                print(i,x)
                if i % x == 0 :
                    print(i,x)
                    one = False
                    x = n+n
                    break
            x += 1

        if one :
             sys.stdout.write(f"1\n{x}\n")
        else:
             sys.stdout.write(f"2\n{n} {n-1}\n")


    t -= 1