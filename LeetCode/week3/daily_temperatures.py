# T: O(n), S: O(n)
class Solution:
    def daily_temperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        res = [0] * n

        stack = []  # (idx, val)
        for idx, val in enumerate(temperatures):
            while stack and val > stack[-1][-1]:
                prev_idx, _ = stack.pop()
                res[prev_idx] = idx - prev_idx

            stack.append((idx, val))

        return res


temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
sol = Solution()
print(sol.daily_temperatures(temperatures))
