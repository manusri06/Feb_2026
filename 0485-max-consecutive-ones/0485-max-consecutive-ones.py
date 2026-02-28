class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = ans = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                l = r+1
            ans = max(ans,r-l+1)
        return ans