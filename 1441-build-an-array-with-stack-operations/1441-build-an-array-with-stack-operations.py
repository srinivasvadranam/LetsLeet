class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        
        
        s = []    #Stores the integers 
        res = []  #stores string i.e., push, pop
        l = 0     #current size of stack
        for i in range(1, n+1):
            s.append(i)
            l += 1
            res.append("Push")
            if target[l-1] != s[-1]:
                res.append("Pop")
                s.pop()
                l -= 1
            elif target == s:
                return res
            
        return res
            
        