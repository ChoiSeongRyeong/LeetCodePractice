class Solution:
    def fillCups(self, amount: List[int]) -> int:
        amount.sort()
        key = amount[0] + amount[1] - amount[2]
        if key <= 0:
            return amount[2]
        else:
            return ceil(key/2) + amount[2]