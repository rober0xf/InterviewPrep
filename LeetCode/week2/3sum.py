# T: O(n^2), S: O(n)
class Solution:
    def three_sum(self, nums: list[int]) -> list[list[int]]:
        trip = set()
        sorted_arr = sorted(nums)

        for i in range(len(nums) - 2):
            left = i + 1
            r = len(nums) - 1

            while left < r:
                current_sum = sorted_arr[i] + sorted_arr[left] + sorted_arr[r]

                if current_sum == 0:
                    current_trip = (sorted_arr[i], sorted_arr[left], sorted_arr[r])
                    trip.add(current_trip)
                    left += 1
                    r -= 1

                elif current_sum > 0:
                    r -= 1
                else:
                    left += 1

        return [list(li) for li in trip]


nums = [-1, 0, 1, 2, -1, -4]
sol = Solution()
print(sol.three_sum(nums))
