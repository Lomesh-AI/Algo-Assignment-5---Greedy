class Solution:
    def fractionalKnapsack(self, val, wt, capacity):
        #code here
        
        n = len(val)
        
        arr = [[val[i]/wt[i], wt[i], val[i]] for i in range(n)]
        arr.sort(reverse=True)
        
        def helper(i, target):
            if target == 0:
                return 0
                
            if i >= n:
                return 0
            
            take = 0
            if arr[i][1] <= target:
                return arr[i][2] + helper(i + 1, target - arr[i][1])
            else:
                return arr[i][0] * target
        
        return helper(0, capacity)    