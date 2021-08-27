""
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.

""
def longestPalindrome(self, s: str) -> str:
        
        def expand_around_center(left,right):
            
            while left>=0 and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1
            
            return s[left+1:right]
                
        length = len(s)
        max_palindrome= ""
        max_length=0
        for i in range(length):
            odd_palindrome= expand_around_center(i,i)
            if len(odd_palindrome)>max_length:
                max_length=len(odd_palindrome)
                max_palindrome=odd_palindrome
            
            even_palindrome = expand_around_center(i,i+1)
            if len(even_palindrome)>max_length:
                max_length=len(even_palindrome)
                max_palindrome=even_palindrome
        return max_palindrome
