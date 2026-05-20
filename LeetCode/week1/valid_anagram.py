from collections import defaultdict


# T: O(n), S: (1)
class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
        s_map = defaultdict(int)
        t_map = defaultdict(int)

        for ch in s:
            s_map[ch] += 1

        for ch in t:
            t_map[ch] += 1

        return s_map == t_map


s = "car"
t = "rat"
sol = Solution()

print(sol.is_anagram(s, t))
