class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        words = s.split()
        if not words:
            return 0
        else:
            last_word = words[len(words)-1]
            return len(last_word)
       
