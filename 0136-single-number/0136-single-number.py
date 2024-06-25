class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        
        size = len(nums)
        
        result = 0

        for num in nums:
            result = result^num

        return result
                
                
nums = [2,2,1]
solution = Solution()

result = solution.singleNumber(nums)
print(result)
        