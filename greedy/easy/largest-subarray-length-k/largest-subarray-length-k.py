class Solution:
    def largestSubarray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        max_idx = nums.index(
            max(nums[:n-k+1])
        )
        return nums[max_idx:max_idx+k]