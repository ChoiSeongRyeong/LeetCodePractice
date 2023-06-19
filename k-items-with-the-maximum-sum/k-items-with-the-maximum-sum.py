class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        if k > numOnes:
            if k > numOnes + numZeros:
                return numOnes - (k - numOnes - numZeros)
            else:
                return numOnes
        else:
            return k