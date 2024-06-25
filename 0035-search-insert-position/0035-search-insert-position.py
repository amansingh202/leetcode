class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        size = len(nums)
        
        for i in range(size):
            if nums[i] == target:
                return i
            elif nums[i]> target:
                return i
            
        else:
            return len(nums)
            
            
solution = Solution()
nums = [1,3,5,6]
target = 7
result = solution.searchInsert(nums,target)
print(result)
                
        