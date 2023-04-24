class Solution:
    def minOperations(self, nums: List[int]) -> int:
        operation_count = 0
        for i in range(1,len(nums)):
            if nums[i-1] < nums[i]:
                continue
            else:
                operation_count += nums[i-1]+1-nums[i]
                nums[i] = nums[i-1]+1
        return operation_count