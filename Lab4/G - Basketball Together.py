import sys

n, d = list(map(int, sys.stdin.readline().split()))

players = list(map(int, sys.stdin.readline().split()))

players.sort()

i, j = 0,n-1
team = 0

while i <= j :

    if players[i] > d :
        team += n
        i = n

    else :
        m = d // players[j]
        i += m
        # print(i,j,m)
        if i <= j :
            j -= 1
            team += 1


sys.stdout.write(str(team)+'\n')
