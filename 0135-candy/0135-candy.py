class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        i = sumi = 1
        while i<n:
            if ratings[i] == ratings[i-1]:
                sumi += 1
                i+=1
                continue
            p = 1
            while i<n and ratings[i] > ratings[i-1]:
                p += 1
                sumi += p
                i+=1
            d = 1
            while i<n and ratings[i] < ratings[i-1]:
                sumi += d
                d += 1
                i+=1
            if d>p:
                sumi += (d-p)
        return sumi

"""n = len(ratings)
c = [1]*n

for i in range(1,n):
    if ratings[i] > ratings[i-1]:
        c[i] = c[i-1]+1

for i in range(n-2,-1,-1):
    if ratings[i] > ratings[i+1]:
        c[i] = max(c[i],c[i+1]+1)
return sum(c) """