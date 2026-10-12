from functools import cache
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        top = len(cost)
        @cache
        def climb(step: int):
            if step >= top:
                return 0
            
            return cost[step] + min(climb(step+1), climb(step+2))

        
        return min(climb(0), climb(1))