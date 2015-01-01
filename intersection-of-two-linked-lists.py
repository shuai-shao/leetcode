# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        if headA == None or headB == None:
            return None
        else:
            checkA = headA
            checkB = headB
            
            present = headA   # count the length of list A
            len_a = 1
            while present.next != None:
                len_a += 1
                present = present.next
            
            present = headB   # count the length of list B
            len_b = 1
            while present.next != None:
                len_b += 1
                present = present.next
            
            if len_a <= len_b:
                for i in range(len_b-len_a):
                    checkB = checkB.next
            else:
                for i in range(len_a-len_b):
                    checkA = checkA.next
            
            found = False
            while not found and checkA != None and checkB != None:
                if not self.isIntersection(checkA, checkB):
                    checkA = checkA.next
                    checkB = checkB.next
                else:
                    found = True
            
            if checkA == None and checkB == None:
                return None
            else:
                return checkA
                    
    def isIntersection(self, checkA, checkB): # helper function to check if checkA and checkB are the intersection nodes
        iterA = checkA
        iterB = checkB
        while iterA!= None and iterB!= None and iterA.val == iterB.val:
            iterA = iterA.next
            iterB = iterB.next
        if iterA != None and iterB != None:
            return False
        else:
            return True
