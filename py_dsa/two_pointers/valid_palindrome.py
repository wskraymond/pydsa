from curses.ascii import isalnum


class Solution:
    '''
        A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters,
        it reads the same forward and backward. Alphanumeric characters include letters and numbers.
    '''
    def isPalindrome(self, s: str) -> bool:
        '''
            Input: s = "A man, a plan, a canal: Panama"
            Output: true
            Explanation: "amanaplanacanalpanama" is a palindrome.

            Input: s = " "
            Output: true
        '''

        n=len(s)
        i,j=0,n-1
        while i<j:
            if not s[i].isalnum():
                i+=1
            elif not s[j].isalnum():
                j-=1
            elif s[i].lower()!=s[j].lower():
                return False
            else:
                i+=1
                j-=1
        return True
