class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runner = 0
        res = []
        for num in nums:
            runner += num
            res.append(runner)
        return res