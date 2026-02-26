class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target = {}

        for i in p:
            if i not in target:
                target[i] = 0
            target[i] += 1

        l = 0
        k = len(p)
        freq = {}
        ans = []
        n = len(s)
        for r in range(n):
            freq[s[r]] = freq.get(s[r],0)+1

            if r-l+1 > k:
                freq[s[l]] -= 1
                if freq[s[l]] == 0:
                    del freq[s[l]]
                l += 1
            if r-l+1 == k:
                if freq == target:
                    ans.append(l)
        return ans

        
