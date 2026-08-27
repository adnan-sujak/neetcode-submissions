class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        list_pop = 2
        for numbers in tokens:
            if numbers not in {"+", "-", "*", "/"}:
                conv = int(numbers)
                stack.append(conv)
            else:
                number1 = stack.pop()
                number2 = stack.pop()

                if numbers =="+":
                    stack.append(number2 + number1)
                elif numbers == "-":
                    stack.append(number2 - number1)
                elif numbers =="*":
                    stack.append(number2 * number1)
                elif numbers =="/":
                    stack.append(int(number2 / number1))
        return stack[0]
