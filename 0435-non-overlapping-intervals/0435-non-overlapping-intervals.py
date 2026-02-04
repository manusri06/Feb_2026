class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        end = []
        for s,e in intervals:
            end.append((e,s))

        end.sort()
        c = 0
        n = len(intervals)
        le = end[0][0]

        for e,s in end[1:]:
            if s<le:
                c+=1
            else:
                le = e
        return c
