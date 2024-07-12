import sys

t = int(sys.stdin.readline().strip())

while t > 0 :

    s = sys.stdin.readline().strip()

    if len(s) == 1:
        print(s)
    else :
        d = {"ab":[], "ba": []}
        u = []
        for i in range(len(s)):
            sub_s = s[i:i+2]
            u.append(s[i])
            # print(sub_s)
            if sub_s == 'ab':
                d["ab"].append(i+1)
            elif sub_s == "ba":
                d["ba"].append(i+1)

        if len(d["ab"]) == len(d["ba"] ):
            sys.stdout.write(s + "\n")

        if len(d["ab"]) > len(d["ba"] ):
                extra = len(d["ab"]) - len(d["ba"] )
                while extra > 0 :
                    idx = d["ab"][0] - 1
                    u[idx] = 'b'
                    d["ab"].pop(0)
                    s = "".join(u)
                    extra -= 1
                sys.stdout.write(s + "\n")
        elif len(d["ab"]) < len(d["ba"]):
                    extra =  len(d["ba"]) - len(d["ab"])
                    while extra > 0:
                            idx = d["ba"][0] - 1
                            u[idx] = 'a'
                            d["ba"].pop(0)
                            s = "".join(u)
                            extra -= 1
            # print(d, s)
                    sys.stdout.write(s + "\n")



    t -=1