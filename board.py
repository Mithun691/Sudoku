import random

def get_valid(boardState,i,j):
    conflicts = []
    #All elements to the left in the row
    for col_id in range(0,j):
        conflicts.append(boardState[i][col_id])
    #All elements above in the column
    for row_id in range(0,i):
        conflicts.append(boardState[row_id][j])
    #All elements in the cell
    top_left=[3*(i//3),3*(j//3)]
    for row_id in range(top_left[0],top_left[0]+3):
        for col_id in range(top_left[1],top_left[1]+3):
            if(row_id<i):
                conflicts.append(boardState[row_id][col_id])
    valid = []
    for k in range(1,10):
        if(k not in conflicts):
            valid.append(k)
    return valid

def randomState(eps=0.5):
    initState = []
    for i in range(0,9):
        initState.append([])
        for j in range(0,9):
            sample = random.random()
            if(sample>eps):
                initState[-1].append('_')
            else:
                valid = get_valid(initState,i,j)
                if(len(valid)==0):
                    initState[-1].append('_')
                else:
                    idx=random.randint(0,len(valid)-1)
                    initState[-1].append(valid[idx])
    return initState

class board:
    def __init__(self,initState):
        self.State = initState

    def __str__(self):
        board_str = ""
        for i in range(9):
            for j in range(9):
                board_str+=str(self.State[i][j])
                board_str+=' '
                if(j%3==2):
                    board_str+=' '
            board_str+='\n'
            if(i%3==2):
                board_str+='\n'
        return board_str

    def get_valid(self,i,j):
        boardState=self.State
        conflicts = []
        #All elements to the left in the row
        for col_id in range(0,9):
            conflicts.append(boardState[i][col_id])
        #All elements above in the column
        for row_id in range(0,9):
            conflicts.append(boardState[row_id][j])
        #All elements in the cell
        top_left=[3*(i//3),3*(j//3)]
        for row_id in range(top_left[0],top_left[0]+3):
            for col_id in range(top_left[1],top_left[1]+3):
                conflicts.append(boardState[row_id][col_id])
        valid = []
        for k in range(1,10):
            if(k not in conflicts):
                valid.append(k)
        return valid

#initState = randomState(0.5)
#Sudoku = board(initState)
#print(Sudoku)
