import sys
n = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
u = {}
c = 0
i, j = 0, n-1
while i <= j:
    if arr[i] not in u :
        c += 1
        u[arr[i]] = 1

    if arr[j] not in u :
        c += 1
        u[arr[j]] = 1
    i += 1
    j -= 1


sys.stdout.write(str(c))

