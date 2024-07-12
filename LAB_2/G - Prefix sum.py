t = int(input().strip())


while t > 0:

    n = int(input())
    arr = [int(i) for i in input().split()]

    p_arr = [arr[0]]

    for i in range(1,n):
        p_arr += [p_arr[i-1] + arr[i]]

    # print(p_arr)
    q = int(input())
    while q > 0 :

        l, r = [int(i)-1 for i in input().split()]
        if l == 0:
            print(p_arr[r])
        else:
            print(p_arr[r] - p_arr[l-1])
        q -= 1

    t -= 1


# 2
# 4
# 10 20 30 40
# 2
# 1 4
# 2 3
# 5
# 1 1 1 1 1
# 3
# 1 2
# 2 5
# 5 5

