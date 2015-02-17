class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        num.sort()
        result= [ ]
        i = 0
        while i < len(num) - 1:
            n1 = num[i]
            target = - n1
            front = i + 1
            rear = len(num) - 1
            while front < rear:
                if num[front] + num[rear] > target:
                    rear = rear - 1
                elif num[front] + num[rear] < target:
                    front = front + 1
                else:
                    n2 = num[front]
                    n3 = num[rear]
                    result.append([n1,n2,n3])
                    while num[front] == n2 and front <len(num)-1:
                        front += 1
                    while num[rear] == n3 and rear > 1:
                        rear -= 1
            while i < len(num)-1 and num[i] == n1:
                i += 1
        return result
