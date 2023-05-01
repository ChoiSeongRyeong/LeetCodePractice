class Solution:
    def splitNum(self, num: int) -> int:
        num = ''.join(sorted(str(num)))
        return sum(map(int, (num[::2], num[1::2])))