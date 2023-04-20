class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter
        chr_dict = Counter(s)
        res = 0
        containsOdd = False
        for k,v in chr_dict.items():
            if v%2 == 1:
                containsOdd = True
            res += v//2 * 2
        return res + int(containsOdd)