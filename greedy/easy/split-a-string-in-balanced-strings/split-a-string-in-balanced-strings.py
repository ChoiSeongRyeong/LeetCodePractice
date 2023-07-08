class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balance, count = 0, 0
        for character in s:
            if character == "R":
                balance += 1
            else:
                balance -= 1
            
            if balance == 0:
                count += 1
        
        return count