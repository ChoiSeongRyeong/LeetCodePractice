class Solution:
    def splitNum(self, num: int) -> int:
        hp = [int(i) for i in str(num)]
        heapify(hp)
        
        n1 = ''
        n2 = ''
        
        while hp:
            n1 += str(heappop(hp))
            if hp:
                n2 += str(heappop(hp))
        
        return int(n1) + int(n2)