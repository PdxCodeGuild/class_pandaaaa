class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        temp = []
        temp2 = []
        for i in range(len(nums)):
            if(nums[i] < target):
                temp.append(i)
        for j in range(len(temp)):
            print (target - nums[temp[j]])
            if (target - nums[temp[j]]) in nums and (target - nums[temp[j]] !=  nums[temp[j]]):
                return [temp[j], nums.index(target-nums[temp[j]])]
            else:
                nums.pop(j)
            
        
        




mySolution = Solution()
print(mySolution.twoSum([5,2,11,4],9))
