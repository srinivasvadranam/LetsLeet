class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        
        
        
        
    
    
    
        
        if len(nums)==1:return nums[0]
        
        if nums[len(nums)-1]<nums[len(nums)-2]:
            return nums[len(nums)-1]
        
        
        
        
        start = 0
        end = len(nums)-1
        
        while start<=end:
            mid = (start+end)//2
            
            
            if nums[mid]>nums[mid+1]:
                return nums[mid+1]
            
            elif nums[mid]>nums[-1]:
                start = mid+1
                
                    
            else:
                end = mid-1
                
        return nums[0]
                



                