import sys

n = int(sys.stdin.readline())


l = 1000000
sum = [1]*l
alldiv = {}
i = 2

while i < l :

    j = i
    while j < l :
        sum[j] += i
        if j not in alldiv:
            alldiv[j] = [1,i]
        else:
            alldiv[j].append(i)
        j += i
    i += 1

print(n, sum[n])
print(alldiv[n])

