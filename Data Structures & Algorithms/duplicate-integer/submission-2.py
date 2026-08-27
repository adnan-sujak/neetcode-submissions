class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for number in nums:
            if number in seen:
                return True
            seen.add(number)

        return False
