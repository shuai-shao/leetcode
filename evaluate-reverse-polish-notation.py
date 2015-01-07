# reverse-polish-notation, aka postfix (polish notation aka prefix)
# use a stack, LIFO
class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        if not tokens:
            return None
        stack = []
        for x in tokens:
            stack.append(x)
            if x in ['+','-','*','/']:
                s = stack.pop()
                b = stack.pop()
                a = stack.pop()
                result = str(self.func(a,b,s))
                stack.append(result)
        return int(stack.pop())
        
    def func(self,a,b,s):    # pretty much self-explanatory 
        if s == '+':
            return int(a) + int(b)
        elif s == '-':
            return int(a) - int(b)
        elif s == '*':
            return int(a) * int(b)
        elif s == '/' and int(b) != 0:
            if int(a)*int(b) >=0:
                return int(a)/int(b)
            else:
                return -1*(-int(a)/int(b))    # -2/3 = -1 in Python, so has to convert to positive 
