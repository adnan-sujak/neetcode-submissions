class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        #return sorted(s) == sorted(t)

        # character counting solution

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0) # at index i in s, the value is 0 if that letter doesn't exist then we add one to that key
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT # compare contents of the two hashmaps
        