class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check every row
        for row in board:
            # row n
            rn=[]
            for n in row:
                if n!='.':
                    rn.append(n)
            if len(rn)!=len(set(rn)):
                return False
        # then compose cols
        for i in range(len(board)):
            # col n
            cn=[]
            # cn=board[0][n]+board[1][n]...
            for row in board:
                if row[i]!='.':
                    cn.append(row[i])
            if len(cn)!=len(set(cn)):
                return False
        # then compose subs, b[i][j],b[i+1][j],b[i+2][j],b[i][j+1]
        for i in range(len(board)): #0,1,2
            sn=[]
            # i/3=rowi...colj, 7/3=2...1,3/3=1...0
            ri=int(i/3)
            cj=int(i%3)
            for row in board[ri*3:(ri+1)*3:]:
                if(row[cj*3]!='.'):
                    sn.append(row[cj*3])
                if(row[cj*3+1]!='.'):
                    sn.append(row[cj*3+1])
                if(row[cj*3+2]!='.'):
                    sn.append(row[cj*3+2])
            if len(sn)!=len(set(sn)):
                return False
        return True
        