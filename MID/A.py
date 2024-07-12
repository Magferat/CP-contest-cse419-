import sys

t = int(sys.stdin.readline())

while t > 0 :
    n = int(sys.stdin.readline())

    arr = list(map(int, sys.stdin.readline().split()))
    s = arr[0]
    not_ugly = True
    i= 1
    while i < n  :

        t = arr[i]
        if s == arr[i] :
            not_ugly = False
            arr[i] = arr[i-1]
            arr[i-1] = t
            i -= 1

        if s != arr[i] :
            not_ugly = True
            s += t
            i += 1

    x = ""
    for i in arr :
        x += str(i) + " "
    if not_ugly :
        print("YES")
        print(x)
    else:
        print("NO")

    t-= 1




