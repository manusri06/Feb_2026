class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dict = {}
        ans = mfreq = l = 0
        for r in range(len(s)):
            if s[r] not in dict:
                dict[s[r]] = 0
            dict[s[r]] +=1
            mfreq = max(mfreq,dict[s[r]])

            while (r-l+1)-mfreq > k:
                dict[s[l]] -= 1
                l+=1
            ans = max(ans,r-l+1)
        return ans










'''n = len(s)
dict = {}
l = 0
ans = mf = 0

for r in range(n):
    if s[r] in dict:
        dict[s[r]] +=1
    else:
        dict[s[r]] = 1
    mf = max(mf,dict[s[r]])
    
    while (r-l+1)-mf > k:
        dict[s[l]] -= 1
        l+=1
    ans = max(ans,r-l+1)
return ans'''



"""  n = len(s)
ans = 0

for i in range(n):
    mf = 0
    freq = [0]*26
    for j in range(i,n):
        indx = ord(s[j])-ord('A')
        freq[indx]+=1
        mf = max(mf,freq[indx])

        if(j-i+1)-mf <= k:
            ans =max(ans,j-i+1)
return ans """
