class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = 0
        r = len(s) - 1

        while(l <= r):
            l_char = s[l].lower()
            r_char = s[r].lower()

            if not l_char.isalnum():
                l += 1
                continue
            
            if not r_char.isalnum():
                r -= 1
                continue

            if l_char != r_char:
                return False
        
            l += 1
            r -= 1

        return True
        

            
