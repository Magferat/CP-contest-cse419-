a = [2,6,-20,7,-5,3,4,-5,-20]

# Given an array "a" , find the maximum sub sumarray sum of lenght k k= 3

p_arr = [0]*len(a)
p_arr[0] = a[0]
i = 1
while i < len(a) :

    p_arr[i] =  a[i] + p_arr[i-1]
    i += 1

p_arr= [0] + p_arr[0::]
print(p_arr)
k = 3
r = k
sum = 0
while r < len(p_arr) :
    s = p_arr[r] - p_arr[r-k]
    if sum < s :
        sum = s
    r += 1
    print(s)


print(sum)
