import sys

t = int(sys.stdin.readline())

while t > 0 :
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    arr.sort()

    i = 1
    if n == 1 :
        print("YES")
    else:
        while i < n-1 :
            if len(arr) == 1:
                print("YES")
                i = n
            else :
                if abs(arr[i] - arr[i-1] ) <= 1 :
                    i += 1
                    n -= 1
                    if n == 1:
                        print("YES")
                        break
                elif abs(arr[i] - arr[i-1] ) > 1:
                    print("NO")
                    break






    t -= 1




# sys.stdout.write(str(n+x))

# print(n,x)

