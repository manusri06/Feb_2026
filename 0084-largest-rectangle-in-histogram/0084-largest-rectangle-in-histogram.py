class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxi = 0
        s = []
        n = len(heights)
        for i in range(n):
            while s and heights[s[-1]]>heights[i]:
                element = heights[s.pop()]
                prev = -1 if not s else s[-1]
                maxi = max(maxi, element*(i-prev-1))
            s.append(i)
        while s:
            element = heights[s.pop()]
            prev = -1 if not s else s[-1]
            maxi = max(maxi, element*(n-prev-1))
        return maxi