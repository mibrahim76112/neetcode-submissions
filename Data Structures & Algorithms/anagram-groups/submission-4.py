class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        
        groups = defaultdict(list)
        

        for word in strs:
            a = [0]*26
            for alphabet in word:
                a[ord(alphabet) - ord("a")] += 1
            groups[tuple(a)].append(word)
        
        return list(groups.values())
            


