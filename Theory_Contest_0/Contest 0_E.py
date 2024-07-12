t = int(input().strip())

while t > 0:
    n = int(input().strip())
    s = input()

    type_1 = 0
    i = 0
    while n > i :
        if s[i] == '#':
            i += 1
        elif s[i] == '.':
            if i+2 < n:
                if s[i] == s[i+1] == s[i+2] == '.':
                    type_1 = 2
                    break
                else:
                    i += 1
                    type_1 += 1

            else:
                type_1 += 1
                i+= 1
    print(type_1)
    t -= 1








