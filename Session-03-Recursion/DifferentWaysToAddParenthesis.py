class Solution:

    def diffWaysToCompute(self, expression: str) -> List[int]:

        result = []

        for i in range(len(expression)):
            ch = expression[i]

            if ch == '*' or ch == '-' or ch == '+':
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i + 1:])

                for l in left:
                    for r in right:
                        if ch == '+':
                            result.append(l + r)
                        elif ch == '*':
                            result.append(l * r)
                        else:
                            result.append(l - r)

        if len(result) == 0:
            result.append(int(expression))

        return result


        