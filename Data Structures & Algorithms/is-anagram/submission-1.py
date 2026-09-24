class Solution:
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