def mex(s):
    m = 0
    while m in s:
        m += 1
    return m

def solve():
    n = int(input())
    sequences = [list(map(int, input().split()))[1:] for _ in range(n)]

    x = 0
    changed = True

    while changed:
        changed = False
        for seq in sequences:
            current_mex = mex(set(seq + [x]))
            if current_mex > x:
                x = current_mex
                changed = True

    print(x)

t = int(input())
for _ in range(t):
    solve()
