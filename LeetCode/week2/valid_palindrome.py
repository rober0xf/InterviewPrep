# T: O(n), S: O(n)
class Solution:
    def is_palindrome(self, s: str) -> bool:
        s = s.strip().lower()
        s_cleaned = "".join(c for c in s if c.isalnum())

        left = 0
        right = len(s_cleaned) - 1
        while left < right:
            if s_cleaned[left] != s_cleaned[right]:
                return False
            left += 1
            right -= 1

        return True


s = " "
sol = Solution()
print(sol.is_palindrome(s))
