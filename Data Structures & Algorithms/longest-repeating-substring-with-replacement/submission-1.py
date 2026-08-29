class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxf = 0
        maxlen = 0
        j = 0
        mapp = {}
        for i in range(len(s)):
            c = s[i]
            if c not in mapp:
                mapp[c] = 0
            mapp[c] += 1
            maxf = max(maxf,mapp[c])

            while ((i-j+1) - maxf) > k:
                mapp[s[j]] -= 1
                j += 1

            maxlen = max(maxlen,i-j+1)
        
        return maxlen

            
             




        