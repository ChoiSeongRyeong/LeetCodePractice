class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        i = cur = count = 0
        while i < len(nums):
            if nums[i] == cur:
                i += 1
                continue
            else:
                cur = nums[i]
                count += 1
                i += 1
        return count