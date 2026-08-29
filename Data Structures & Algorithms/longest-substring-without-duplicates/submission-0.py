class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mapp = {}
        output = 0
        j = 0
        for i in range(len(s)):
            c = s[i]
            if c not in mapp:
                mapp[c] = 0
            mapp[c] += 1

            while mapp[c] > 1:
                mapp[s[j]] -= 1
                j += 1

            output = max(output,i-j+1)

        return output