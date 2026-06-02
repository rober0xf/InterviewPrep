# T: O(n), S: O(n)
class Solution:
    def is_valid(self, s: str) -> bool:
        hs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        if s[0] in hs:
            return False

        stack = []
        for c in s:
            if c in hs:
                if stack and stack[-1] == hs[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return len(stack) == 0


s = "([)]"
sol = Solution()
print(sol.is_valid(s))
