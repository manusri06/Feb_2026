class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l = maxi = z =  0

        for r in range(n):
            if nums[r] == 0:
                z+=1
            while z>k:
                if nums[l] == 0:
                    z-=1
                l+=1
            maxi = max(maxi,r-l+1)
        return maxi