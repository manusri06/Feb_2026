class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        n = len(s)
        ans = 0
        ss = set()
        for r in range(n):
            if s[r] not in ss:
                ss.add(s[r])
                ans = max(ans,r-l+1)
            else:
                while s[r] in ss:
                    ss.remove(s[l])
                    l+=1
                ss.add(s[r])
        return ans
            

        