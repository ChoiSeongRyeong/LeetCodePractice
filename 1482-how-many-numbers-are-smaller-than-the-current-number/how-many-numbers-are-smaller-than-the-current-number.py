class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] > nums[j]: ans[i] += 1
                elif nums[i] < nums[j]: ans[j] += 1
                else: continue
        return ans