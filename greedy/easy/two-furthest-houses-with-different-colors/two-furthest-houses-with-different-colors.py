class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        left, right = 0, len(colors)-1
        while colors[left] == colors[right]:
            left += 1
            if colors[left] == colors[right]:
                right -= 1
            else:
                return len(colors)-1-left
        return right