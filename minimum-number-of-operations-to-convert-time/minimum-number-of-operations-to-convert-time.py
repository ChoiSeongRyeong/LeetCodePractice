class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        def convert_str_to_timestamp(time: str)-> int:
            return int(time[:2])*60 + int(time[-2:])
        current_timestamp = convert_str_to_timestamp(current)
        correct_timestamp = convert_str_to_timestamp(correct)
        diff = abs(current_timestamp - correct_timestamp)
        res = 0
        for n in [60,15,5,1]:
            res += diff // n
            diff %= n
        return res