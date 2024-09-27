import sys

n = int(sys.stdin.readline())
coins = list(map(int, sys.stdin.readline().split()))
coins.sort(reverse=True)

total = sum(coins)
# print(coins)
count = 0
m = 0
for c in coins :

    if m <= total :
        m += c
        total -= c
        count += 1

print(count)
