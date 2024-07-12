import sys
n = input()

arr = list(map(int, sys.stdin.readline().split()))

u = {}

for i in arr:
    if i not in u:
        u[i] = 1

x = list(u)
print(len(x))


