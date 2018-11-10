class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """        
        
        def candidates(board,idx):
            for i in range(len(board)):
                for j in range(len(board)):
                    if board[i][j]=='.':
                        idx[0]=i
                        idx[1]=j
                        return True
            return False
        
        def to_fill(board,row,col,num):  
            for j in range(len(board)):
                if board[row][j]== num:
                    return False
            for i in range(len(board)):
                if board[i][col]== num:
                    return False
            #block_id=(row/3)*3+col/3
            block_list=[]
            for bi in range(3):
                for bj in range(3):
                    block_list.append(board[row - row % 3+bi][col - col % 3+bj])
            for k in range(len(block_list)):
                if block_list[k]==num:
                    return False           
            return True   
        def solve(board):
            idx=[0,0]        
            if not candidates(board,idx):
                #print (board)
                return True

            for num in range(1,10):
                num_str=str(num)
                if to_fill(board,idx[0],idx[1],num_str):
                    board[idx[0]][idx[1]]=num_str
                    if  solve(board): 
                        return True
                board[idx[0]][idx[1]]='.'
            return False

        if solve(board):
            print (board) 
                 
                    
                    
            