# def permute(s, l, r):
#     # Base case: if l is equal to r, print the permutation
#     if l == r:
#         print("".join(s))
#     else:
#         print(s)
#         # Generate permutations
#         for i in range(l, r + 1):
#             # Swap characters at indices l and i
#             s[l], s[i] = s[i], s[l]
#             # Recurse with the next index
#             permute(s, l + 1, r)
#             # Backtrack (undo the swap)
#             s[l], s[i] = s[i], s[l]
#
# # Driver code
# s = list("ABC")
# n = len(s)
# permute(s, 0, n - 1)


def perm(s,l,r) :


    if l == r :
        print("".join(s))

    for i in range(l, r+1):
        s[l], s[i] = s[i], s[l]
        perm(s,l+1,r)
        c += 1
        s[l], s[i] = s[i], s[l]
s = list("ABCD")
perm(s,0,len(s)-1)