def solve_N_rook(n,index):
    board=[[True]*n]*n
    for i in range(n):
        for t in range(n):
            if board[i][t]:
                #invalid position to place a rook
                for l in range(n):
                    board[l][t]=False
                for m in range(n):
                    board[i][m]=False