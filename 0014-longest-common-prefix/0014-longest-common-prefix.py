class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if not strs:
            return ""
        
        prefix = strs[0]
        
        for string in strs[1:]:
            while string.find(prefix) != 0:
                prefix = prefix[:-1]
                
                if not prefix:
                    return ""
                
        return prefix

    
solution = Solution()

strs = ["flower","flow","flight"]

result = solution.longestCommonPrefix(strs)
print(result)
        