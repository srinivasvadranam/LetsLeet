class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key = len)
        temp = strs[0]
    
        res = ""
        for i in range(len(temp)):
            temp_char = temp[i]
            
            for j in range (1, len(strs)):
                if strs[j][i] == temp_char:
                    continue
                
                else :
                    return res
                    
            res += temp_char
        return res