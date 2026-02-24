class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = sum(nums[0:k])
        maxi = s
        n = len(nums)
        for i in range(k,n):
            s = s-nums[i-k]+nums[i]
            maxi = max(s,maxi)
        return maxi/k