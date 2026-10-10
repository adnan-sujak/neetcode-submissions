class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        group = {}
        
        for index, word in enumerate(strs):
            key = tuple(sorted(word)) 
            # strings are immutable, use sorted and store in another var
            # returns a list - can't use as dict key
            
            # dict keys must be hashable, but lists are mutable and therefore
            # cannot be keys
            # hashable means a value that can never be changed


            # all anagrams produce the same result, so when sorted, they all
            # share one dict key

            if key not in group:
                group[key] = []
            # avoiding missing key error

            group[key].append(word) 
            # each key map to list of words, not just one index
        return list(group.values())