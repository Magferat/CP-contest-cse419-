t = int(input().strip())


while t > 0:

    n,k = [int(i) for i in input().strip().split()]
    arr = [int(i) for i in input().strip().split()]
    b = sorted(arr)
    c = sorted(arr, reverse=True)

    if k >= 2:
        print('YES')

    else:
        if arr == b :
            print("YES")

        else:
            print('NO')

    t -= 1