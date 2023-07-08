from bisect import bisect_right
from itertools import accumulate


class Solution:
    def answerQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        nums.sort()
        nums = list(accumulate(nums))
        return [bisect_right(nums, q) for q in queries]  # bisect_right(A, e) returns largest i s.t., for x in A[i:], e < x


