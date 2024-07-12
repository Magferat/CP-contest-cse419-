import sys

n, q = list(map(int, sys.stdin.readline().split()))
items = list(map(int, sys.stdin.readline().split()))
items.sort()
p_items = items[::]
for i in range(1,n):
    p_items[i] += p_items[i-1]

while q > 0 :
    buy, free = list(map(int, sys.stdin.readline().split()))
    if buy == n :
        sys.stdout.write(str(p_items[free-1]) + "\n")
    elif buy == 1 :

            sys.stdout.write(str(items[(n-2)]) + "\n")
    else:
        cart = p_items[n-1]-p_items[-(buy+2)]
        discount = cart - items[-(free-1)]

        sys.stdout.write(str(discount) + "\n")
    q -= 1