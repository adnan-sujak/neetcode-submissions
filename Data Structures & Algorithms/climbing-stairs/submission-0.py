
from functools import cache
class Solution:
    def climbStairs(self, n: int) -> int:
        
        @cache
        def down(steps:int):
            if steps == 2:
                return 2
            if steps == 1:
                return 1
            return down(steps-1) + down(steps - 2)
        return down(n)

