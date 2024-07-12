# array sorted "a" of length N. find two numbers such that ai + aj = k (o < i, j < N and i != j

# a = [5,10,15,20,25]
a = [2,3,4,11,14,15,30,40]
n = len(a)
k = 25


i, j = 0, n-1

while i < j :

    sum = a[i] + a[j]

    if sum < k :
        i += 1
    elif sum > k :
        j -= 1
    else:
        print(a[i], a[j], a[i] + a[j])
        i = j







