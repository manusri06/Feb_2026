class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        n = len(s)
        maxi = 0
        cset = set()

        for r in range(n):
            if s[r] not in cset:
                cset.add(s[r])
                maxi = max(maxi,r-l+1)
            else:
                while s[r] in cset:
                    cset.remove(s[l])
                    l+=1
                cset.add(s[r])
        return maxi
        