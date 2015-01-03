class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    # notice: e.g. 1.2 < 1.10, 10.6.5 > 10.6, 1.0 = 1
    def compareVersion(self, version1, version2):
        group1 = version1.split('.')
        group2 = version2.split('.')
        
        if len(group1) > len(group2):    # to make sure group1 and group2 have the same length
            group2.extend(['0']*(len(group1)-len(group2)))
        if len(group2) > len(group1):
            group1.extend(['0']*(len(group2)-len(group1)))
            
        compare = 0 
        stop = False
        while group1 and group2 and not stop:
            a1 = int(group1.pop(0))
            a2 = int(group2.pop(0))
            if a1 > a2:
                compare = 1
                stop = True
            elif a1 < a2:
                compare = -1 
                stop = True 
                
        return compare
