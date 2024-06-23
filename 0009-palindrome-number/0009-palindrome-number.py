class Solution:
    def isPalindrome(self, x: int) -> bool:
        original_str = str(x)

        reversed_str = original_str[::-1]

        return original_str == reversed_str


solution = Solution()

num = 123

result = solution.isPalindrome(num)

print(result)

        