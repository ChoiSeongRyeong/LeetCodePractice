class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        expected_ene = sum(energy)+1

        expected_exp = 1
        exp_cum = 0
        for exp in experience:
            expected_exp = max(expected_exp, (exp-exp_cum)+1)
            exp_cum += exp

        return(
            max(0, expected_ene-initialEnergy)
            +max(0, expected_exp-initialExperience)
        )