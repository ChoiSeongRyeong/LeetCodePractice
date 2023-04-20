class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        arr_sum = sum(arr)
        if arr_sum % 3 != 0:
            return False
        else:
            n_arr = len(arr)
            expected_part_sum = arr_sum / 3
            part_sum = 0
            part_sum_count = 0
            for i in range(n_arr):
                part_sum += arr[i]
                if part_sum == expected_part_sum:
                    part_sum = 0
                    part_sum_count += 1
                else:
                    continue
            
            if part_sum_count >= 3:
                return True
            else:
                return False
