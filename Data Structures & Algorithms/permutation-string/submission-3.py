class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        mapp1 = {}
        mapp2 = {}

        for i in range(len(s1)):
            mapp1[s1[i]] = mapp1.get(s1[i], 0) + 1
            mapp2[s2[i]] = mapp2.get(s2[i], 0) + 1

        if mapp1 == mapp2:
            return True

        j = 0

        for i in range(len(s1), len(s2)):
            mapp2[s2[i]] = mapp2.get(s2[i], 0) + 1
            mapp2[s2[j]] -= 1
            if mapp2[s2[j]] == 0:
                del mapp2[s2[j]]
            j += 1

            if mapp1 == mapp2:
                return True

        return False