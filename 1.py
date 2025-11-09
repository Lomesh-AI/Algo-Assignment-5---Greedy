class Solution:    
    def minPlatform(self, arr, dep):
        # code here
        
        p = 0
        maxx = 0
        
        arr.sort()
        dep.sort()
        
        n = len(arr)
        m = len(dep)
        
        i = 0
        j = 0
        
        while i < n and j < n:
            if arr[i] <= dep[j]:
                p += 1
                i += 1
            else:
                p -= 1
                j += 1
            maxx = max(maxx, p)    
        
        return maxx