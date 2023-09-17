class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum(money_in_a_bank) for money_in_a_bank in accounts])