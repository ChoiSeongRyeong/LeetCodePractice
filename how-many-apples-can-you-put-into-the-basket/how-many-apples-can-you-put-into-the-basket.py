class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()
        total, count = 5000, 0
        for i in range(len(weight)):
            total -= weight[i]
            if total < 0:
                return count
            else:
                count +=1
        return count