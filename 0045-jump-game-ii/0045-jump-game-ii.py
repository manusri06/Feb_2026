class Solution:
    def jump(self, nums: List[int]) -> int:

        j = f = ce = 0

        for i in range(len(nums)-1):
            f = max(f,i+nums[i])
            if i == ce:
                j+=1
                ce = f
        return j 

""" def rec(i):
    if i > len(nums)-1:
        return 0 
    ans = float('inf')
    for step in range(1,nums[i]+1):
        ans += min (ans,rec(i+step))
    return ans
return rec(0) """

