import sys

n = int(sys.stdin.readline())

for inq in range(n):
    ps = sys.stdin.readline().strip()
    depot = []
    is_vps = True

    for char in ps:
        if char == "(":
            depot.append(char)
        elif char == ")":
            if len(depot) == 0:
                is_vps = False
                break
            else:
                depot.pop()

    if is_vps == True and len(depot) == 0 :
        print("YES")
    else:
        print("NO")


