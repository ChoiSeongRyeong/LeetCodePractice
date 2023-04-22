class Solution:
    def maximum69Number (self, num: int) -> int:
        num_str_list = list(str(num))
        for i in range(len(num_str_list)):
            if num_str_list[i] == "6":
                num_str_list[i] = "9"
                return int("".join(num_str_list))
        return int("".join(num_str_list))
