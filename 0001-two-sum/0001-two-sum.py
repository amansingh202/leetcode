class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

        return []

#object creation for Solution class
solution = Solution()
nums = [2,7,11,15]
target = 9

#result
result = solution.twoSum(nums,target)
print(result)
    

        