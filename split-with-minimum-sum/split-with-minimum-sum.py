class Solution:
    def splitNum(self, num: int) -> int:
        copy = [int(x) for x in str(num)]
        copy.sort()
        num1 = 0
        num2 = 0
        for i in range(0,len(copy)):
            if i %2 == 0:
                num1 = num1*10 + copy[i]
            elif i %2 !=0:
                num2 = num2*10 + copy[i]
        return num1 + num2