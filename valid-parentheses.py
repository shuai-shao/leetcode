class Solution:
    # @return a boolean
    def isValid(self, s):
        if not s:
            return True
        else:
            stack = []
            balanced = True
            i = len(s)
            while i>0 and balanced:
                i = i -1
                par = s[i]
                if par in [')','}',']']:
                    stack.append(par)
                elif not stack:
                    balanced = False
                else:
                    top = stack[-1]
                    if not self.matches(par,top):
                        balanced = False
                    else:
                        stack.pop()
            if balanced and not stack:
                return True
            else:
                return False
                   
    def matches(self,left,right):
        opens = '([{'
        closers = ')]}'
        return opens.index(left) == closers.index(right)
                   
