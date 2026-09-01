class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid_index = left + ((right - left) // 2)
            middle_num = nums[mid_index]
            
            if middle_num == target:
                return mid_index
            elif middle_num < target:
                left = mid_index + 1
            else: # middle_num > target
                right = mid_index - 1
        return -1
            




