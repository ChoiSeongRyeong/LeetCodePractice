class Solution:
    def minOperations(self, nums: List[int]) -> int:
        left_max = nums[0]
        operation_count = 0
        for i in range(1,len(nums)):
            if left_max < nums[i]:
                left_max = nums[i]
                continue
            else:
                operation_count += left_max-nums[i]+1
                left_max += 1
        return operation_count