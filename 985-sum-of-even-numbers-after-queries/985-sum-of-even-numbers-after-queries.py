class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        q = queries
        total = 0
        for j in nums:
                if j%2 == 0:
                    total += j
                    
                    
        for i in range (len(q)):
            temp = nums[q[i][1]]
            nums[q[i][1]] = nums[q[i][1]] + q[i][0]
            
            if temp%2 == 0 and nums[q[i][1]]%2 != 0:
                total = total - temp
                
                
                
            elif temp%2 != 0 and nums[q[i][1]]%2 == 0:
                total = total + nums[q[i][1]]
                
                
            elif temp%2 == 0 and nums[q[i][1]]%2 == 0:
                total = total - temp + nums[q[i][1]]
            
            res.append(total)
        return res