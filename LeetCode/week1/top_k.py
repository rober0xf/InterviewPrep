from collections import defaultdict
from heapq import heapify, heappop, heappush


# T: O(n*log k), S: O(n)
class Solution:
    def top_k_frequent(self, nums: list[int], k: int) -> list[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        h = []
        heapify(h)
        for key, v in count.items():
            heappush(h, (v, key))

        while len(h) > k:
            heappop(h)

        return [item[1] for item in h]


nums = [1, 2, 1, 2, 1, 2, 3, 1, 3, 2]
sol = Solution()
print(sol.top_k_frequent(nums, 2))
