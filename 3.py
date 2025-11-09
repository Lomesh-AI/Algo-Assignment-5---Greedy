t = int(input())

for _ in range(t):
    length = int(input())
    bob = list(map(int, input().split(' ')))
    alice = list(map(int, input().split(' ')))
    
    if bob == alice or bob == alice[::-1]:
        print('Bob')
    else:
        print("Alice")