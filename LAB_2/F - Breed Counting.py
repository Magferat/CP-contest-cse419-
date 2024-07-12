t, q = [int(i) for i in input().strip().split()]

arr = [[0]*t,[0]*t,[0]*t]
p_arr = [[0]*t,[0]*t,[0]*t]

n = 0
while n < t:

    cow = int(input().strip()) - 1

    arr[cow][n] = 1
    if n == 0 :
        p_arr[0][0] =  arr[0][0]
        p_arr[1][0] =  arr[1][0]
        p_arr[2][0] =  arr[2][0]

    else:
        p_arr[0][n] =  p_arr[0][n-1] + arr[0][n]
        p_arr[1][n] =  p_arr[1][n-1] + arr[1][n]
        p_arr[2][n] =  p_arr[2][n-1] + arr[2][n]


    n += 1

while q > 0:

    start, end =  [int(i)-1 for i in input().strip().split()]

    if start == 0:
        a = p_arr[0][end]
        b = p_arr[1][end]
        c = p_arr[2][end]
    else:

        a = p_arr[0][end] - p_arr[0][start-1]
        # print( p_arr[0][end] , p_arr[0][start])
        b = p_arr[1][end] - p_arr[1][start-1]
        c = p_arr[2][end] - p_arr[2][start-1]
    print(a,b,c)
    q -= 1


