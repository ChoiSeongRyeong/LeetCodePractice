class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        n_odd, n_even = 0, 0
        for i in range(len(position)):
            if position[i] % 2 == 0:
                n_even += 1
            else:
                n_odd += 1
        return min(n_odd, n_even)
            