import sys

t = int(sys.stdin.readline())


while t > 0 :

    n, k = list(map(int, sys.stdin.readline().split()))

    a_arr = list(map(int, sys.stdin.readline().split()))
    b_arr = list(map(int, sys.stdin.readline().split()))

    a_arr.sort()
    b_arr.sort()
    r = 0
    if k == 0 :
        r = sum(a_arr)

    elif k == n and a_arr[-1] < b_arr[0] :
         r = sum(b_arr)

    elif a_arr[0] >= b_arr[-1] :
         r = sum(a_arr)
    else:
        i,j = 0, n-1

        while a_arr[i] < b_arr[j] and k > 0 :

            a_arr[i] = b_arr[j]
            i += 1
            j -= 1
            k -= 1

        r = sum(a_arr)
    sys.stdout.write(str(r)+"\n")

    t -= 1





