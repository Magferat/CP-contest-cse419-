n = 10

def f(n):
    if n == 0 :
        return 0
    elif n == 1 :
        return 1
    else:
        return f(n-1) + f(n-2)

for i in range(n+1) :
    print(f(i))

print("=========")
def f2(n) :
    if n == 1 : return 1
    elif n == 0 : return 0

    return f2(n-1) + f2(n-2)

print(f2(n))



