class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        n = len(nums)
        total = sum(nums)
        sub_sum = 0
        subsequence = []
        nums.sort()
        for i in range(n-1, -1, -1):
            subsequence.append(nums[i])
            sub_sum += nums[i]
            total -= nums[i]
            if sub_sum > total:
                return subsequence