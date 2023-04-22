class Solution:
    def maximum69Number (self, num: int) -> int:
        num_str = str(num)
        idx_to_change = num_str.find("6")
        if idx_to_change == -1:
            return num
        else:
            return num + 3 * 10**(len(num_str)-1-idx_to_change)
