class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans = ''
        for c in s:
            if c.isalnum():
                c = c.lower()
                ans += c
            else:
                continue
        
        return ans == ans[::-1]