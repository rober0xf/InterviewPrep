# T: O(n), S: O(n)
class Solution:
    def contains_duplicate(self, nums: list[int]) -> bool:
        uniques = set()
        for num in nums:
            if num in uniques:
                return True
            uniques.add(num)

        return False


nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
sol = Solution()
print(sol.contains_duplicate(nums))
