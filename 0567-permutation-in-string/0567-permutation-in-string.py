class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        target = {}
        for i in range(len(s1)):
            if s1[i] not in target:
                target[s1[i]] = 0
            target[s1[i]] += 1

        current = {}
        l = 0
        for r in range(len(s2)):
            current[s2[r]] = current.get(s2[r],0)+1

            if r-l+1 > k:
                current[s2[l]]-=1
                if current[s2[l]] == 0:
                    del current[s2[l]]
                l+=1
            if r-l+1 == k:
                if current == target:
                    return True
        return False

