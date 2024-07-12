n,m,k = [int(i) for i in input().split()]

dem = [int(i) for i in input().split()]
sup = [int(i) for i in input().split()]


d,s = 0, 0

sum = 0


while s < m and d <n :
    # print(sup[s])
    a,b = sup[s] -k, sup[s] + k

    if a == dem[d] or b == dem[d] :
        sup.pop(s)
        dem.pop(d)
        s += 1
        d += 1
    else :
        if d + 1 == n :
            d = 0
            s += 1
        else:
            d += 1


print(sum)


