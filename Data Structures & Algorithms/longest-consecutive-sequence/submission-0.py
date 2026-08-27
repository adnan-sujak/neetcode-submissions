class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0

        for num in nums:
            if (num - 1) not in s:
                length = 0
                while (num + length) in s:
                    length += 1
                longest = max(length, longest)
        return longest


        

        

        
        
        # stack
        # 2
        # 20
        # 4
        # 10

        # if stack.next() != stack.previous + 1, stack.pop