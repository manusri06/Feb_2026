class Solution:
    def jump(self, nums: List[int]) -> int:

        j = f = ce = 0

        for i in range(len(nums)-1):
            f = max(f,i+nums[i])
            if i == ce:
                j+=1
                ce = f
        return j