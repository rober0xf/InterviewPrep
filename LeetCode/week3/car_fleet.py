# T: O(n logn), S: O(n)
class Solution:
    def car_fleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = sorted(zip(position, speed, strict=True), reverse=True)
        print(cars)
        stack = []

        for p, s in cars:
            time_dest = (target - p) / s  # decimal div
            stack.append(time_dest)

            # if they collide
            if len(stack) >= 2 and stack[-1] <= stack[-2]:  # noqa: PLR2004
                stack.pop()

        return len(stack)


target = 12
position = [10, 8, 0, 5, 3]
speed = [2, 4, 1, 1, 3]
sol = Solution()
print(sol.car_fleet(target, position, speed))
