class infix_prefix():
    def precedence(self, ch):
        if ch == '+' or ch == '-':
            return 1
        elif ch == '*' or ch == '/':
            return 2
        return 0

    def infixToPostfix(self, s):
        stack = []
        result = ""

        for ch in s:

            # operand
            if ch.isalpha():
                result += ch

            # opening bracket
            elif ch == '(':
                stack.append(ch)

            # closing bracket
            elif ch == ')':
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.pop()

            # operator
            else:
                while stack and self.precedence(stack[-1]) >= self.precedence(ch):
                    result += stack.pop()
                stack.append(ch)

        while stack:
            result += stack.pop()

        return result

    def infixToPrefix(self, s):

        # Step 1: reverse
        s = s[::-1]

        # Step 2: swap brackets
        new_s = ""
        for ch in s:
            if ch == '(':
                new_s += ')'
            elif ch == ')':
                new_s += '('
            else:
                new_s += ch

        # Step 3: postfix
        postfix = self.infixToPostfix(new_s)

        # Step 4: reverse postfix
        prefix = postfix[::-1]

        return prefix
    
if __name__=='__main__':
    obj=infix_prefix()
    print(obj.infixToPrefix("(a+b)*c"))