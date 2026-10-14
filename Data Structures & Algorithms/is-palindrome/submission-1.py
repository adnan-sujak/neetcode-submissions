class Solution:
    def isPalindrome(self, s: str) -> bool:
        forward = [c.lower() for c in s if c.isalnum()]
        return forward == list(reversed(forward))
