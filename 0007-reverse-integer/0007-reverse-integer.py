class Solution:
    def reverse(self,x:int) -> int:
        reversed_digit = 0
        is_neg = x<0
        x = abs(x)
        while(x!=0):
            digit = x%10
            reversed_digit = reversed_digit*10 + digit
            x //= 10

        if is_neg:
            reversed_digit = -reversed_digit

        if reversed_digit < -2**31 or reversed_digit > 2**31 - 1:
            return 0

        return reversed_digit


x = -123  
solution = Solution()
result = solution.reverse(x)
print(result)