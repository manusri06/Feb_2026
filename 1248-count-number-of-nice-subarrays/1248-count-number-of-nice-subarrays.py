class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        ps = 0
        count = {0:1}
        ans = 0

        for num in nums:
            if num%2 == 1:
                ps+=1
            if ps-k in count:
                ans += count[ps-k]
            if ps in count:
                count[ps]+=1
            else:
                count[ps] = 1
        return ans
