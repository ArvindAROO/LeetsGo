class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        local = 0
        prev = -1
        maxi = 0
        for i in nums:
            if i == 1:
                local += 1
            else:
                if local + prev > maxi:
                    maxi = prev + local
                else:
                    pass
                
                prev = local
                local = 0
                    
        if prev + local > maxi:
            return prev + local
        
        return maxi
    