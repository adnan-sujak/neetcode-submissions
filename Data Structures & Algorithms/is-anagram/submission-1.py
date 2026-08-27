class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        firstString = {}
        secondString = {}

        for i in range(len(s)):
            firstString[s[i]] = 1 + firstString.get(s[i], 0)
            secondString[t[i]] = 1 + secondString.get(t[i], 0)

        return firstString == secondString


        
        