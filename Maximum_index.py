class Solution:
    def maxIndexDiff(self, a, n):
        pre_min = [0] * n
        suff_max = [0] * n
        
        maxi = a[n - 1]
        for i in range(n - 1, -1, -1):
            maxi = max(maxi, a[i])
            suff_max[i] = maxi
        
        mini = a[0]
        for i in range(n):
            mini = min(mini, a[i])
            pre_min[i] = mini
        
        i, j = 0, 0
        ans = -1
        while i < n and j < n:
            if pre_min[i] <= suff_max[j]:
                ans = max(ans, j - i)
                j += 1
            else:
                i += 1
        return ans
