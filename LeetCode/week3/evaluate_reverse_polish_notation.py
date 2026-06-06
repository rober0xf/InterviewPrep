# T: O(n), S: O(n)
class Solution:
    def eval_rpn(self, tokens: list[str]) -> int:
        operands = {"+", "-", "*", "/"}
        stack = []

        for v in tokens:
            if v not in operands:
                stack.append(int(v))
            else:
                v1 = stack.pop()
                v2 = stack.pop()
                if v == "+":
                    stack.append(v2 + v1)
                elif v == "-":
                    stack.append(v2 - v1)

                elif v == "*":
                    stack.append(v2 * v1)

                else:
                    stack.append(int(v2 / v1))

        return int(stack[0])


tokens = ["4", "13", "5", "/", "+"]
sol = Solution()
print(sol.eval_rpn(tokens))
