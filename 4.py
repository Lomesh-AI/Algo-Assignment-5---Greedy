t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split(' ')))
    maxx = 0        
    for i in range(0, n, 2):
        maxx = max(maxx, arr[i])
        
    print(maxx)            
    