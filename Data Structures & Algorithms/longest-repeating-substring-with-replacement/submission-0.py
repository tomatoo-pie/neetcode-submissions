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

            if (((i-j)+1) - maxf) <= k:
                maxlen = max(maxlen,i-j+1)

            while ((i-j+1) - maxf) > k:
                mapp[s[j]] -= 1
                maxf = mapp[s[j]]
                j += 1
                for it in mapp:
                    maxf = max(maxf,mapp[it])
        
        return maxlen

            
             




        