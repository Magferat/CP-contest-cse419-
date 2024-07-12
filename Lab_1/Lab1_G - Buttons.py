t = int(input().strip())


while t > 0:

    buttons = [int(i) for i in input().split()]

    if buttons[2] % 2 != 0:
        if buttons[0] >= buttons[1] :
            print('First')
        else:
            print('Second')

    else:
        if buttons[0] <= buttons[1] :
            print('Second')

        else:
            print('First')

    t -= 1