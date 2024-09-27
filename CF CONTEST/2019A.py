import sys

t = int(sys.stdin.readline())

while t > 0 :

    n = int(sys.stdin.readline())
    balls = list(map(int,sys.stdin.readline().split()))

    red_0 = 0
    red_0_max = 0
    red_1 = 0
    red_1_max = 0

    i = 0

    while i < n :
        if i % 2 == 0 :
            red_0 += 1
            if red_0_max < balls[i] :
                red_0_max = balls[i]
        else:
            red_1 += 1
            if red_1_max < balls[i]:
                red_1_max = balls[i]
        i += 1

    ans1 = red_1 + red_1_max
    ans0 = red_0 + red_0_max

    ans = max(ans0,ans1)
    sys.stdout.write(str(ans)+"\n")



    t -= 1