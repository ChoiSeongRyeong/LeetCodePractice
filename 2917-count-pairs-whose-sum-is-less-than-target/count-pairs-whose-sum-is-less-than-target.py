class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        n = len(nums)

        count = sum(
            sum(
                1 if num + nums[j] < target else 0
                for j in range(i+1, n)
            )
            for i, num in enumerate(nums[:-1])
        )
        return count