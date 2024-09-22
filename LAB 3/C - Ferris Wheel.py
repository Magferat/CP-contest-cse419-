import sys

n,x = list(map(int, sys.stdin.readline().split()))
child = list(map(int, sys.stdin.readline().split()))

child.sort()

count = 0

i,j = 0, n-1

while i <= j :

    w = child[i] + child[j]

    if w <= x :
        count += 1
        i += 1
        j -= 1
    elif w > x :
        if child[j] <= x :
            count += 1
        j -= 1




sys.stdout.write(str(count)+"\n")

# print(n,x)

