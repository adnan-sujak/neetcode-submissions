from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #count = Counter(nums)

        #return [number for number, frequency in count.most_common(k)]

        count = {}
        # count each number
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        # sort numbers by frequency, highest first

        numbers = sorted(count, key=count.get, reverse=True)

        return numbers[:k]
        
        

