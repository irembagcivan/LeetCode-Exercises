class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i] + nums[j] == target:
                    return [i,j]
                
solution = Solution()

print(solution.twoSum([2, 7, 11, 15], 9)) 

        
    