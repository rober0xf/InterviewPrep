# T: O(n*log n), S: O(1)
class Solution:
    def two_sum(self, numbers: list[int], target: int) -> list[int]:
        for left in range(len(numbers) - 1):
            w_left = left + 1
            w_right = len(numbers) - 1

            while w_left <= w_right:
                mid = w_left + (w_right - w_left) // 2
                curr = numbers[left] + numbers[mid]

                if curr == target:
                    return [left + 1, mid + 1]
                if curr < target:
                    w_left = mid + 1
                else:
                    w_right = mid - 1

        return []


numbers = [2, 3, 4]
sol = Solution()
print(sol.two_sum(numbers, 6))
