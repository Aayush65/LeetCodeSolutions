class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        n=len(words)
        ans=[]
        i=0
        while i<n:
            temp=[]
            seen=0
            cur=""
            while i<n and seen+len(words[i])+len(temp)<=maxWidth:
                temp.append(words[i])
                seen+=len(words[i])
                i+=1

            m=len(temp)
            if (m-1)!=0 and i!=n:
                q,r=divmod(maxWidth-seen,(m-1))
                sp=[q+(1 if j<r else 0) for j in range(m-1)]
                for j in range(m-1):
                    cur+=temp[j]+' '*sp[j]
                cur+=temp[-1]

            else:
                for j in range(m-1):
                    cur+=temp[j]+' '
                cur+=temp[-1]
                cur+=' '*(maxWidth-len(cur))

            ans.append(cur)
        return ans              