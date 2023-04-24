class Solution:
    def minOperations(self, nums: List[int]) -> int:
        left_max = nums[0]
        operation_count = 0
        for i in range(1,len(nums)):
            operation_count += max(0, left_max-nums[i]+1)
            left_max = max(left_max+1, nums[i])
        return operation_count