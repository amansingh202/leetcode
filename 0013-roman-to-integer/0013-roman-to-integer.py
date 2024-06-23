class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        
        prev_value = 0
        total = 0
        
        for char in reversed(s):
            current_val = roman_map[char]
            
            if current_val < prev_value:
                total -= current_val
                
            else:
                total += current_val
                
            prev_value = current_val
                
                
        return total
    
    
solution = Solution()

ip = 'MCMXCIV'

result = solution.romanToInt(ip)

print(result)
        