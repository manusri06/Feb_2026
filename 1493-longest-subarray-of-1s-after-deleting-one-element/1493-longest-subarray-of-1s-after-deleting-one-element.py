class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        k = 1
        l = 0
        ans = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                k-=1
            while k<0:
                if nums[l] == 0:
                    k += 1
                l+=1
            ans = max(ans,r-l)
        return ans