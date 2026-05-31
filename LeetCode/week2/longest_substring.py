# T: O(N), S: O(N)
class Solution:
    def length_of_longest_substring(self, s: str) -> int:
        if len(s) == 1:
            return 1

        count = 0
        p1 = 0
        p2 = 0

        chars = set()
        while p2 < len(s):
            while s[p2] in chars:
                count = max(count, len(chars))
                chars.remove(s[p1])
                p1 += 1

            chars.add(s[p2])
            count = max(count, len(chars))
            p2 += 1

        return count


s = "au"
sol = Solution()
print(sol.length_of_longest_substring(s))
