class Solution:
    def reverseWords(self, s):
        words = s.split()
        words = words[::-1]
        return " ".join(words)



    
        