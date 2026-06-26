class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return {char: s.count(char) for char in s} == {char: t.count(char) for char in t}