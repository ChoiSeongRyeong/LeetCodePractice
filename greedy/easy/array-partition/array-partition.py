class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # Set boundary
        K = 10000
        # Consider negative numbers
        count = [0] * (2 * K + 1)
        for element in nums:
            count[K + element] += 1

        Sum = 0
        is_evenindex = True
        for i in range(len(count)):
            while count[i] > 0:
                if is_evenindex:
                    Sum += i - K
                count[i] -= 1
                is_evenindex = not is_evenindex

        return Sum