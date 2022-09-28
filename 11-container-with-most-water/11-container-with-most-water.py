class Solution:
    def maxArea(self, height: List[int]) -> int:
        nums = height
        h1 = 0
        h2 = len(nums)-1
        max_s = 0
        
        while h1<h2:
            x = min(nums[h1],nums[h2]) * (h2-h1)
            if x>max_s:
                max_s = x
            if nums[h1]<nums[h2]:
                h1 += 1
            else:
                h2 -= 1
                
        return max_s