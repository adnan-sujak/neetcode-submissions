class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #my_map = {}


        return loop_through_array(nums)

      
        

def loop_through_array(nums: List[int]):
    my_map = {}
    for number in nums:
        my_map[number] = my_map.get(number, 0) + 1
        #yield number
        if my_map[number] > 1:
            return number