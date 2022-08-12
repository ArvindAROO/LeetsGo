class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        t = nums.count(0)
        if t > 1:
            return [0] * len(nums)
        if t == 1:
            index = nums.index(0)
            nums.remove(0)
            sol = nums[0]
            for i in nums[1:]:
                sol *= i
            nums = [0] * (len(nums) + 1)
            nums[index] = sol
            return nums
        sol = nums[0]
        for i in nums[1:]:
            sol *= i
        final =[sol // i for i in nums]
        
        return final