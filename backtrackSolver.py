from board import *

def backtrackSolve(Sudoku):
    for i in range(9):
        for j in range(9):
            if(Sudoku.State[i][j]=='_'):
                valid=Sudoku.get_valid(i,j)
                for val in valid:
                    Sudoku.State[i][j]=val
                    isValid,solvedSudoku=backtrackSolve(Sudoku)
                    if(isValid):
                        return [isValid,solvedSudoku]
                    else:
                        Sudoku.State[i][j]='_'
                return False,Sudoku
    
    for i in range(9):
        for j in range(9):
            if(Sudoku.State[i][j]=='_'):
                return False,Sudoku
    return True,Sudoku


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

isValid,solvedSudoku = backtrackSolve(Sudoku)

if(isValid):
    print(solvedSudoku)