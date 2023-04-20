class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        i = 0
        while (k > 0) and (i < n):
            if nums[i] < 0:
                nums[i] = -nums[i]
                i += 1
                k -= 1
            else:
                break
        
        if k > 0:
            if i == 0:
                nums[i] = nums[i] * (-1)**(k%2)
            elif i == n:
                nums[i-1] = nums[i-1] * (-1)**(k%2)
            elif nums[i] >= nums[i-1]:
                nums[i-1] = nums[i-1] * (-1)**(k%2)
            else:
                nums[i] = nums[i] * (-1)**(k%2)
        
        return sum(nums)