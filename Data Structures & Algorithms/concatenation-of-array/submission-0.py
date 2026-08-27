class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)


        for _ in range(2):
            for number in nums:
                ans.append(number)
                
        return ans