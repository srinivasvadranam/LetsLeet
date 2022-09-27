class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        lst = []
        # l = [[0,0,0]]
        # if nums == [0,0,0,0]:
        #     return l
        for i in range (len(nums)):
            if  i>0 and nums[i-1] == nums[i]:
                
                continue
            j = i+1
            k = len(nums)-1
            while j<k:
                sum1 = nums[i]+nums[j]+nums[k]
                if sum1 > 0:
                    k = k-1
                elif sum1<0:
                    j += 1
                else:
                    # print("OK")
                    lst.append([nums[i],nums[j],nums[k]])
                    j += 1
                    while nums[j-1] == nums[j] and j<k :
                        j += 1
                    # break
            # print("OK123")
        return lst
    


