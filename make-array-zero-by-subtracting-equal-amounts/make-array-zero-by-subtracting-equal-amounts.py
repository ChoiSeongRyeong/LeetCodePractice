class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums_dict = {}
        for num in nums:
            nums_dict[num] = 0
        if 0 in nums_dict.keys():
            return len(nums_dict.keys())-1
        else:
            return len(nums_dict.keys())