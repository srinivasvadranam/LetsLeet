class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c1 = 0
        c2 = 0
        maj1 = maj2 = "0"
        for i in range(len(nums)):
            
            if nums[i] == maj1:
                c1 += 1
                
            elif nums[i] == maj2:
                c2 += 1
                
            elif c1 == 0:
                maj1 = nums[i]
                c1 += 1
            
            elif c2 == 0:
                maj2 = nums[i]
                c2 += 1
            
            else:
                c1 -= 1
                c2 -= 1
                
            # print(maj1, maj2, c1, c2)
            
        a1 = a2 =0
        for i in range(len(nums)):
            if nums[i] == maj1:
                a1 += 1
            elif nums[i] == maj2:
                a2 += 1
                
        # print(maj1, maj2)
        

        res = []
        if a1>len(nums)/3:
            res.append(maj1)
            
        if a2>len(nums)/3:
            res.append(maj2)
            
        return res
                
            

            
                
            
        