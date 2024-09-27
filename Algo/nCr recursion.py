def nCr(n,r) :

    if r > n: return 0
    if r == 0 or r == n : return 1

    return nCr(n-1, r-1) + nCr(n-1, r)

print(nCr(5,4))