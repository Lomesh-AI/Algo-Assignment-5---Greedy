def valid_k(a, k):
    mod_values = set(x % k for x in a)
    return len(mod_values) == 2

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()

    candidates = []
    for i in range(n):
        for j in range(i + 1, n):
            diff = a[j] - a[i]
            if valid_k(a, diff):
                candidates.append(diff)

    if candidates:
        print(min(candidates))
    else:
        print(10**18)
