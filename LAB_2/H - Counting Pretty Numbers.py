t = int(input())

while t > 0:

    l,u = [int(i) for i in input().split()]
    n = 0
    for i in range(l, u+1):
        if i % 10 == 2 or i % 10 == 3 or i % 10 == 9:
            n += 1
    print(n)

    t -= 1

# 2
# 1 10
# 11 33

