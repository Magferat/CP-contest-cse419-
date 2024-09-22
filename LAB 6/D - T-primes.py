import sys

t = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

for num in arr:
    if num == 1 :
        sys.stdout.write("NO\n")
    else:
        k = num
        fact = []
        i = 2
        while i * i <= num:
            while num % i == 0:
                fact.append(i)
                num //= i
            i += 1
        if num > 1:
                fact.append(num)

        f = set(fact)
        f = list(f)
        c = k
        print(f)
        for i in f :

            a = 1-1/i
            c *= a
            # print(i,c, a)

        print(f, c)












