class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        ans = ""
        for i in words:
            ans += i[::-1]
            ans += " "
            
        return ans[0:-1]
        