class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        if colors[0] != colors[-1]:
            return len(colors) - 1

        res: int = 0
        for i, color in enumerate(colors):
            if color != colors[0]:
                res = max(res, i, len(colors) - 1 - i)
            
        return res   