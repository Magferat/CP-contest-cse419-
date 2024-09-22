import sys

n,m,k = list(map(int, sys.stdin.readline().split()))

arr_n = list(map(int, sys.stdin.readline().split()))
arr_m = list(map(int, sys.stdin.readline().split()))
arr_n.sort()
arr_m.sort()
print(arr_n)
print(arr_m)

x = 0
n -= 1

available = [0]*10000000

for i in arr_m :
    available[i] += 1
    print(available[i],i)



for i in arr_n :
    if x <= m :
        if available[i] >= 1 :
            x += 1
            available[i] -= 1
        elif available[i-k] >= 1 :
            x += 1
            available[i-k] -= 1

        elif available[i+k] >= 1 :
            x += 1
            available[i+k] -= 1
        print(i, i-k, i+k)

sys.stdout.write(str(x)+"\n")
