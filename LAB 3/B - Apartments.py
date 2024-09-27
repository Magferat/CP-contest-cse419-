import sys

n,m,k = list(map(int, sys.stdin.readline().split()))

arr_n = list(map(int, sys.stdin.readline().split()))
arr_m = list(map(int, sys.stdin.readline().split()))
arr_n.sort()
arr_m.sort()


count = 0

i, j = 0,0

while i < m and j < n:

    up = arr_m[i] + k
    low = arr_m[i] - k

    app = arr_n[j]
    if low <= app <= up :
        j += 1
        i += 1
        count += 1
    else :
        if up < app :
            i += 1
        if low > app :
            j += 1

print(count)


