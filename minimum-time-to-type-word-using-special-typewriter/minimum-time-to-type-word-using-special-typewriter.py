class Solution:
    def minTimeToType(self, word: str) -> int:
        character_dict = {
            "abcdefghijklmnopqrstuvwxyz"[i]:i
            for i in range(26)
        }

        cur_c = "a"
        time = 0
        for c in word:
            time += min(
                abs(character_dict[c] - character_dict[cur_c]),
                26 - abs(character_dict[c] - character_dict[cur_c])
            ) + 1
            cur_c = c
        return time