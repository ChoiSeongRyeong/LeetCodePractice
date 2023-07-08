class Solution:
    def fillCups(self, amount: List[int]) -> int:
        amount.sort()
        gap = amount[2]-amount[1]

        if amount[0] <= gap:
            return amount[0] + max(amount[2] - amount[0], amount[1])
        else:
            return (amount[0] - gap) // 2 + (amount[0] - gap) % 2 + amount[2]