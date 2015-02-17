class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        if len(num) < 3:
            return sum(num)
        num.sort()
        ans  = num[0] + num[1] + num[2]
        for i in range(len(num)-1):
            front = i + 1
            rear = len(num) -1
            while front < rear:
                sum = num[i] + num[front] + num[rear]
                if abs(sum - target) < abs(ans-target):
                    ans = sum
                if sum-target ==0:
                    return sum
                if sum - target > 0:
                    rear = rear - 1
                if sum - target < 0:
                    front = front + 1
        return ans
