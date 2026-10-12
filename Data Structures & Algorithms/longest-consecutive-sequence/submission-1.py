class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        
        longest = 0

        for left in numbers:
            smaller_left = left -1
            if smaller_left in numbers:
                continue
            current = left
            count = 1
            while current + 1 in numbers:
                count +=1
                current +=1
            if count > longest:
                longest = count
        return longest
        
            
            
