class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        ind1, ind2 = 0, -1
        size = len(colors)
        while ind1 < size:
            front = colors[ind1]
            if front != colors[-1]:
                return size - ind1 - 1
            last = colors[ind2]
            if last != colors[0]:
                return size + ind2
            ind1 += 1
            ind2 -= 1