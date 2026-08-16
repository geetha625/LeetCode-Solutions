class Solution(object):
    def stoneGameIX(self, stones):
        count = [0, 0, 0]
        for stone in stones:
            count[stone % 3] += 1
        count0 = count[0]
        count1 = count[1]
        count2 = count[2]
        if count0 % 2 == 0:
            return count1>0 and count2>0
        return abs(count1 - count2) > 2