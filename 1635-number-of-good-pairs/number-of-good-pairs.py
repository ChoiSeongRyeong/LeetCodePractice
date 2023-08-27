class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        num_dict = dict()
        for num in nums:
            if num not in num_dict:
                num_dict[num] = 1
            else:
                num_dict[num] += 1
        result = 0
        for k,v in num_dict.items():
            result += v*(v-1)//2
        return result