class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = dict()
        for st in strs:
            key = tuple(sorted(st))
            if key in anagram_map:
                anagram_map[key].append(st) 
            else:
                anagram_map[key] = [st]
        return [v for k,v in anagram_map.items()]
 
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            s_map = {k:0 for k in s}
            t_map = {k:0 for k in t}
            if s_map.keys() == t_map.keys():
                for k in s:
                    s_map[k] += 1
                for k in t:
                    t_map[k] += 1
                return s_map == t_map
            return False
        return False
        