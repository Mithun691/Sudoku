from board import *

def fillObvious(Sudoku):
    ctr=1
    while(ctr>0):
        ctr=0
        for i in range(9):
            for j in range(9):
                if(Sudoku.State[i][j]=='_'):
                    valid=Sudoku.get_valid(i,j)
                    if(len(valid)==1):
                        Sudoku.State[i][j]=valid[0]
                        ctr+=1;
    return Sudoku

initState = [[5,3,'_','_',7,'_','_','_','_'],
             [6,'_','_',1,9,5,'_','_','_'],
             ['_',9,8,'_','_','_','_',6,'_'],
             [8,'_','_','_',6,'_','_','_',3],
             [4,'_','_',8,'_',3,'_','_',1],
             [7,'_','_','_',2,'_','_','_',6],
             ['_',6,'_','_','_','_',2,8,'_'],
             ['_','_','_',4,1,9,'_','_',5],
             ['_','_','_','_',8,'_','_',7,9]]

Sudoku = board(initState)
print(Sudoku)

partialSudoku = fillObvious(Sudoku)
print(partialSudoku)