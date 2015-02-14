class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        dic = {}
        result = []
        for i in range(len(strs)):
            key= ''.join(sorted(strs[i]))
            if key not in dic:
                dic[key] = [strs[i]]
            else:
                dic[key].append(strs[i])
        for key in dic:
            if len(dic[key])>=2:
                result.extend(dic[key])    
        return result
        
