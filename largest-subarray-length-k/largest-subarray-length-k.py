class Solution:
    def largestSubarray(self, nums: List[int], k: int) -> List[int]:
        
        import numpy as np
        n = len(nums)
        
        max_idx = np.argmax(nums[:n-k+1])
        return nums[max_idx:max_idx+k]