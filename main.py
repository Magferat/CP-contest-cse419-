# t = int(input().strip())
#
# while t > 0 :
#
#     a,b = input().strip().split()
#     x = b[0:1] + a[1::]
#     y = a[0:1] + b[1::]
#     print(x,y)
#     t-= 1

# D. Manhattan Circle

t = int(input().strip())

while t > 0 :
    n, m = [int(i) for i in input().strip().split()]
    arr = []

    x = 0
    while x < n :

        p = input().strip()
        arr += [p]
        x += 1

    # print(arr)

    i, j = 0,0
    print(len(arr), arr[0][1])

    t -= 1






