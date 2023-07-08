class Solution:
    def splitNum(self, num: int) -> int:
        digits = sorted(str(num))
        return (int("".join(d for d in digits[::2])) +
                int("".join(d for d in digits[1::2])))