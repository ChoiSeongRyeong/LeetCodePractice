class Solution:
    def splitNum(self, num: int) -> int:
        digits = sorted(list(str(num)))
        return (
            int("".join(digits[::2]))
            + int("".join(digits[1::2]))
        )