class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0

        # Initialize the first pointer (slow) at the first element
        slow = 0

        # Iterate over the array with the second pointer (fast)
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]

        # Length of the array without duplicates
        length = slow + 1

        # Modify the original list to contain only unique elements followed by underscores
        for i in range(length, len(nums)):
            nums.append('_')

        # Print and return the length of unique elements
        print(length)
        print(nums)  # Print only the unique elements
        return length

solution = Solution()
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
solution.removeDuplicates(nums)
