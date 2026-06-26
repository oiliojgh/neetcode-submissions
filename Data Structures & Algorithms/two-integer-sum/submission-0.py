class Solution:
    def twoSum(self, s: List[int], t: int) -> List[int]:
        has = {}
        for i, n in enumerate(s):
            if t - n in has:
                return [has[t - n], i]
            has[n] = i