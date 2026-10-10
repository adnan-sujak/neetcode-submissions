class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #for idx, val in enumerate(nums):
         #   last_index = len(nums) - 1 
          #  if idx >= last_index:
           #     return
            #if nums[idx] + nums[idx+1] == target:
             #   return [idx, idx+1]

        #brute force

        #for i in range(len(nums)):
         #   for j in range(i+1, len(nums)): #start loop after i which will always mean i < j
          #      if nums[i] + nums[j] == target:
           #         return [i,j]
        
        prevMap = {}

        for i, n in enumerate(nums):
            diff = target - n 
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i