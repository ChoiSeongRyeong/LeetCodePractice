class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        i = 0
        while i < len(number)-1:
            if number[i] == digit:
                if number[i] < number[i+1]:
                    return number[:i]+number[i+1:]
                else:
                    target_idx = i
                    i += 1
            else:
                i += 1

        if number[-1] == digit:
            target_idx = i

        return number[:target_idx]+number[target_idx+1:]