class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        for c in t:
            if c not in s:
                return ""

        mapt = {}

        for c in t:
            mapt[c] = mapt.get(c, 0) + 1

        cnt = 0
        j = 0
        minlen = ""

        for i in range(len(s)):
            c = s[i]

            if c in mapt:
                if mapt[c] > 0:
                    cnt += 1
                mapt[c] -= 1

            while cnt == len(t):

                if minlen == "" or i - j + 1 < len(minlen):
                    minlen = s[j:i+1]

                if s[j] in mapt:
                    mapt[s[j]] += 1

                    if mapt[s[j]] > 0:
                        cnt -= 1

                j += 1

        return minlen