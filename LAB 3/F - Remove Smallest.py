import sys

t = int(sys.stdin.readline())

while t > 0 :
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    arr.sort()
    i = 1
    if n == 1 :
        sys.stdout.write("YES\n")
    else:
        while i <= n-1 :
            if arr[i] - arr[i-1] <= 1 :
                i += 1

            else :
                sys.stdout.write("NO\n")
                break

        if i == n :
            sys.stdout.write("YES\n")

    t -= 1





