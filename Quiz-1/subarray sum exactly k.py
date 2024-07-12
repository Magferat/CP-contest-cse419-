
a = [5,2,3,10,1,7,3]

p_arr = [0]*(len(a))

p_arr[0] = a[0]

i = 1

while i < len(a) :

    p_arr[i] = p_arr[i-1] + a[i]
    i += 1
p_arr = [0] + p_arr[0::]
print(p_arr)

l = 0
r = 1
k  =  18
while r > l :

    s = p_arr[r] - p_arr[l]

    if s == k :
        print(l,r-1, p_arr[l], p_arr[r], s)
        r = l
    elif s > k :
        l += 1
    elif s < k :
        r += 1

    print(s)




