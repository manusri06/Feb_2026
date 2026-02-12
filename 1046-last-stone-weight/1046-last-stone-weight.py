class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)>1:
            stones.sort()
            x = stones[-1]
            y = stones[-2]
            stones.remove(x)
            stones.remove(y)
            stones.append(x-y)
        return stones[0]