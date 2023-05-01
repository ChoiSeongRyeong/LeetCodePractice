class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        diff = (
            (int(correct[:2])*60 + int(correct[-2:]))
            -(int(current[:2])*60 + int(current[-2:])) 
        )
        res = 0
        for n in [60,15,5,1]:
            res += diff // n
            diff %= n
        return res