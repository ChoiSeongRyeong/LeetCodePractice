class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        expected_ene = sum(energy)+1

        expected_exps = []
        exp_cum = 0
        for exp in experience:
            expected_exps.append(exp-exp_cum)
            exp_cum += exp
        expected_exp = max(expected_exps)+1

        return(
            max(0, expected_ene-initialEnergy)
            +max(0, expected_exp-initialExperience)
        )