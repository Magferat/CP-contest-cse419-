a = [2,6,-20,7,-5,3,4,-5,-20]

# Given an array "a" , find the maximum sub sumarray

p_arr = [0]*len(a)
p_arr[0] = a[0]
i = 1
while i < len(a) :
    p_arr[i] =  a[i] + p_arr[i-1]
    i += 1
p_arr= [0] + p_arr[0::]
print(p_arr)

l = 0
r = 1
i = 0
sum = 0
while r < len(p_arr) :

    s = p_arr[r] - p_arr[l]

    if p_arr[r] < p_arr[l] :
        l = r
    if sum < s :
        sum = s

    r += 1

print(sum)


# if says to show index

l = 0
r = 1
max = [0,0,0]
while r < len(p_arr) :

    sum = p_arr[r] - p_arr[l]
    if sum > max[2] :
        max[0] = l
        max[1] = r
        max[2] = sum
    if p_arr[r] < p_arr[l]  :
        l = r
    r+= 1

print("Maximum Sum", max[2])
print("Index: from", max[0], "to", max[1]-1)


