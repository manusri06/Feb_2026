class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        dict = {}
        maxi = 0
        l = 0

        for r in range(n):
            if fruits[r] in dict:
                dict[fruits[r]]+=1
            else:
                dict[fruits[r]] = 1
            
            while len(dict)>2:
                dict[fruits[l]] -=1
                if dict[fruits[l]] == 0:
                    del dict[fruits[l]]
                l+=1
            maxi = max(maxi,r-l+1)
        return maxi