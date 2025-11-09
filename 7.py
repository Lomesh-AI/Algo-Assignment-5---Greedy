t = int(input())
 
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    rating = arr[n-2]
    
    for i in range(n-2):
        red -= arr[i]
        
    print(arr[n-1] - red)    