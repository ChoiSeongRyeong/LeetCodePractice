class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        
        ans = 0

        for i in range(1, len(colors)):
            if colors[i] != colors[0]:
                ans =  max(ans, len(colors)-1-i, i)

        return ans