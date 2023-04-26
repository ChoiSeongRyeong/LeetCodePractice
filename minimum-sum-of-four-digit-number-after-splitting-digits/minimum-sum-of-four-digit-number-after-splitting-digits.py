class Solution:
    def minimumSum(self, num: int) -> int:
        digits = sorted(list(str(num)), key=lambda x: int(x))
        return (
            int(reduce(
                lambda a,v: a+v, digits[::2], ''
            ))+
            int(reduce(
                lambda a,v: a+v, digits[1::2], ''
            ))
        )