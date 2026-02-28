class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ss = set()
        n = len(s)
        l = 0
        maxi = 0
        for r in range(n):
            if s[r] not in ss:
                ss.add(s[r])
                maxi = max(r-l+1,maxi)
            else:
                while s[r] in ss:
                    ss.remove(s[l])
                    l+=1
                ss.add(s[r])
        return maxi
                
        