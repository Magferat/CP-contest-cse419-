t = int(input().strip())

while t > 0 :
    n = int(input().strip())
    x = [int(i) for i in input().split()]

    if x[0] == 1:
        print("YES")
    else:
        print("NO")

    t-= 1