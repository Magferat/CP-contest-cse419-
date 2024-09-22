import  sys

t = int(sys.stdin.readline())


while t > 0 :

    arr = list(map(int, sys.stdin.readline().split()))

    i = 0

    while i < 5 :

        m_idx = arr.index(min(arr))
        arr[m_idx] += 1
        i += 1

    s = arr[0] * arr[1] * arr[2]
    print(s)
    t-= 1
