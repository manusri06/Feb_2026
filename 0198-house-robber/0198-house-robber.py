class Solution:
    def rob(self, nums: List[int]) -> int:
        a = 0
        b = 0
        for i in range(len(nums)):
            c = max(b,nums[i]+a)
            a = b
            b = c
        return b