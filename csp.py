import btSolver as bt
domain = []
changed = False
def reduceRows(row, col):
    global domain
    global changed
    e = domain[row][col][0]
    for i in range(9):
        try:
            if(len(domain[row][i])>1):
                (domain[row][i].remove(e))
                changed = True
        except:
            pass

def reduceColumns(row, col):
    global domain
    global changed
    e = domain[row][col][0]
    for i in range(9):
        try:
            if(len(domain[i][col])>1):
                (domain[i][col].remove(e))
                changed = True
        except:
            pass
        
def reduceBoxes(row, col):
    global domain
    global changed
    e = domain[row][col][0]
    for i in range((row//3)*3, (row//3)*3+3):
        for j in range((col//3)*3, (col//3)*3+3):
            try:
                if(len(domain[i][j])>1):
                    (domain[i][j].remove(e))
                    changed = True
            except:
                pass

def invalid(puzz):
    for i in range(9):
        for j in range(9):
            if(puzz[i][j]!=0):
                for k in range(9):
                    if(k!=i and puzz[k][j]==puzz[i][j]):
                        return True
                    if(k!=j and puzz[i][k]==puzz[i][j]):
                        return True
                for p in range(i//3, i//3+3):
                    for q in range(j//3, j//3+3):
                        if(p!=i and q!=j and puzz[i][j]==puzz[p][q]):
                            return True

def reduceDomain(puzzle):
    global domain
    global changed
    unhandled=[[True for i in range(9)] for j in range(9)]
    #fixing domain of initially filled cells
    for i in range(9):
        for j in range(9):
            if (puzzle[i][j]!=0):
                domain[i][j]=[puzzle[i][j]]
    #reducing domain as much as possible
    #print('Domain', domain)
    changed = True
    while(changed):
        changed = False
        for i in range(9):
            for j in range(9):
                if(len(domain[i][j])==1 and unhandled[i][j]):
                    reduceRows(i,j)
                    reduceColumns(i,j)
                    reduceBoxes(i,j)
                    unhandled[i][j]=False
        

def solveSudoku(puzzle):
    global domain
    if invalid(puzzle):
        print("Invalid Puzzle")
        return puzzle
    #print(puzzle)
    domain = [[list(range(1,10)) for i in range(9)] for j in range(9)]
    reduceDomain(puzzle)
    solution = bt.solve(domain)
    return solution
