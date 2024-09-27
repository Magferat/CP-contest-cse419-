import sys

l1 = [2,4,3]
l2 = [5,6,4]

r = 0
def add_two(l1,l2,i,res) :
    print(i, l1[i], l2[i],res)
    if i == len(l1) - 1 :
        return l1[i] + l2[i]

    res += 10 * i * add_two(l1,l2,i+1,res)
    print(i, l1[i], l2[i],res, "h2")
    return res

d = add_two(l1,l2,0,r)
print(d)
print(r)