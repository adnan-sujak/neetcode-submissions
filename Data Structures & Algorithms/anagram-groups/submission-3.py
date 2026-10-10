class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        group = {}
        
        for index, word in enumerate(strs):
            key = tuple(sorted(word)) 
            # strings are immutable, use sorted and store in another var
            # returns a list - can't use as dict key

            if key not in group:
                group[key] = []

            group[key].append(word) 
            # each key map to list of words, not just one index
        return list(group.values())