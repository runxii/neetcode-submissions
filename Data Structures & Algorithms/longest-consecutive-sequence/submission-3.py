class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        seq=[]
        # former sequence
        fseq=seq
        # sorted nums without repeated elements
        # positive nums
        pn=[n for n in nums if n>=0]
        # negative nums
        nn=[-n for n in nums if n<0]
        # sorted negative nums
        snn=[n for n in set(nn)]
        sn=[-x for x in sorted(snn,reverse=True)]+sorted(list(set(pn)))
        print(sn)
        if len(sn)==1:
            return 1
        for i in range(len(sn)-1):
            # if is sequence, push it to seq
            if sn[i]+1==sn[i+1]:
                if sn[i] not in seq:
                    seq.append(sn[i])
                seq.append(sn[i+1])
                print(seq)
            # if not sequence, save the former seq and create a new seq
            else:
                seq=[]
            if len(seq)>len(fseq):
                fseq=seq
        print(fseq)
        return len(fseq)