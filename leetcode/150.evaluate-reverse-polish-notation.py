#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
# Solution 1: Stack
# Time: O(N) | Space: O(N)
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return tokens[0]
        op = ["+", "-", "*", "/"]
        st = []
        for token in tokens:
            if token in op:
                num2 = int(st.pop(-1))
                num1 = int(st.pop(-1))
                if token == "+":
                    curNum = num1 + num2
                elif token == "-":
                    curNum = num1 - num2
                elif token == "*":
                    curNum = num1 * num2
                else:
                    curNum = int(num1 / num2)
                st.append(str(curNum))
            else:
                st.append(token)
        return st.pop()


# Solution 1-2: Stack with lambda function
def evalRPN(self, tokens: List[str]) -> int:
    operations = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "/": lambda a, b: int(a / b),
        "*": lambda a, b: a * b
    }

    stack = []
    for token in tokens:
        if token in operations:
            number_2 = stack.pop()
            number_1 = stack.pop()
            operation = operations[token]
            stack.append(operation(number_1, number_2))
        else:
            stack.append(int(token))
    return stack.pop()
# @lc code=end
