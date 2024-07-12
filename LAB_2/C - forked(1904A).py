import sys

t = int(sys.stdin.readline())
moves = []
while t > 0:

    ka,kb = list(map(int, sys.stdin.readline().split()))
    king_x, king_y = list(map(int, sys.stdin.readline().split()))
    qx, qy = list(map(int, sys.stdin.readline().split()))
    attack_king = [(king_x-ka, king_y-kb), (king_x-ka, king_y+kb), (king_x+ka, king_y-kb), (king_x+ka, king_y+kb), (king_x - kb, king_y - ka), (king_x - kb, king_y + ka), (king_x + kb, king_y - ka), (king_x + kb, king_y + ka) ]
    attack_queen = [(qx-ka, qy-kb), (qx-ka, qy+kb), (qx+ka, qy-kb), (qx+ka, qy+kb), (qx - kb, qy - ka), (qx - kb, qy + ka), (qx + kb, qy - ka), (qx + kb, qy + ka) ]

    common = {}
    c = 0
    for mv in attack_king :
        if mv in attack_queen:
            if mv not in common :
                common[mv] = 1
                c += 1


    print(c)

    t -= 1
