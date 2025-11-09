import string
class Solution:
    def smallestString(self, s: str) -> str:
        
        found = False
        n = len(s)
        arr = [s[i] for i in range(n)]

        letters = 'abcdefghijklmnopqrstuvwxyz'
        mapping = {letters[i]: letters[i-1] for i in range(len(letters))}

        for i in range(n):
            if arr[i] != 'a':
                arr[i] = mapping[arr[i]]
                found = True
            elif found and arr[i] == 'a':
                return ''.join(arr) 

        if not found:
            arr[-1] = 'z'

        return ''.join(arr)