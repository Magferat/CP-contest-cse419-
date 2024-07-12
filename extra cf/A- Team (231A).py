t = int(input().strip())
c = 0

while t > 0 :

    n = [int(i) for i in input().strip().split()]
    x = sum(n)
    if x >= 2 :
        c += 1
    t -= 1
print(c)
