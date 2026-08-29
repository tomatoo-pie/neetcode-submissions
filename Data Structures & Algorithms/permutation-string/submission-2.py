class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        mapp1 = {}
        mapp2 = {}

        for i in range(len(s1)):
            mapp1[s1[i]] = mapp1.get(s1[i], 0) + 1
            mapp2[s2[i]] = mapp2.get(s2[i], 0) + 1

        j = 0

        for i in range(len(s1), len(s2)):
            found = True

            for k in range(len(s1)):
                c = s1[k]

                if c not in mapp2 or mapp1[c] != mapp2[c]:
                    found = False
                    break

            if found:
                return True

            mapp2[s2[i]] = mapp2.get(s2[i], 0) + 1

            mapp2[s2[j]] -= 1
            j += 1

        # Check the final window
        found = True

        for k in range(len(s1)):
            c = s1[k]

            if c not in mapp2 or mapp1[c] != mapp2[c]:
                found = False
                break

        return found