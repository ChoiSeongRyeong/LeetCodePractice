class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        i = 0
        for i in range(len(number)-1):
            if number[i] == digit:
                if number[i] < number[i+1]:
                    return number[:i]+number[i+1:]
                target_idx = i

        if number[-1] == digit:
            target_idx = i+1

        return number[:target_idx]+number[target_idx+1:]