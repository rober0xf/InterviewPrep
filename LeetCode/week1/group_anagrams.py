from collections import defaultdict


# T: O(N*K*Log k), S: O(N*K)
class Solution:
    def group_anagrams(self, strs: list[str]) -> list[list[str]]:
        store = defaultdict(list)

        for s in strs:
            s_sorted = "".join(sorted(s))
            store[s_sorted] += [s]

        return list(store.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
sol = Solution()

print(sol.group_anagrams(strs))
