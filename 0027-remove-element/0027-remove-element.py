class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        size = len(nums)
        i = 0
        while i < size:
            if nums[i] == val:
                del nums[i]
                size -= 1
            else:
                i += 1
        output  = len(nums)
        
        print(output)
        diff = size - len(nums)
        strArr = repr(nums)
        for j in range(diff):
            strArr.append('_')
            
        print(strArr)
        

solution = Solution()

nums = [0,1,2,2,3,0,4,2]
val = 2

solution.removeElement(nums, val)