# T: O(n), S: O(n)
class Solution:
    def daily_temperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        res = [0] * n

        stack = []
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                res[idx] = i - idx

            stack.append(i)

        return res


temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
sol = Solution()
print(sol.daily_temperatures(temperatures))
