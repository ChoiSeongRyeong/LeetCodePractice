class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        left, right = 0, len(colors)-1
        while colors[left] == colors[right]:
            left += 1
        max_distance_from_right = right - left

        left, right = 0, len(colors)-1
        while colors[left] == colors[right]:
            right -= 1
        max_distance_from_left = right - left
        return max(max_distance_from_right, max_distance_from_left)