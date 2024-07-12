t = int(input().strip())

while t > 0:
    n = int(input().strip())

    if n % 3 == 0 :
        print('Second')
    else:
        print('First')
    t -= 1