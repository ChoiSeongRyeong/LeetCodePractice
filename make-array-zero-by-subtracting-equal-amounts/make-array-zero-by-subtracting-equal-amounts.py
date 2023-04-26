class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums_set = set()
        for num in nums:
            if num != 0:
                nums_set.update([num])
        return len(nums_set)