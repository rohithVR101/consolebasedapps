import random
import time
import puzzles

def display_grid(li):
    count=0
    print("| - - - - - - - - - - - |")
    for i in li:
        for j in i:
            if(count == 0):
                print("|",end=" "),
            print(j, end = " ")
            if(count in [2,5,8]):
                    print("|",end=" "),
            count+=1
        print()
        if li.index(i) in [2,5]:
            print("| - - - + - - - + - - - |")
        elif li.index(i) == 8:
            print("| - - - - - - - - - - - |")
        count=0

def has_empty(arr,l):
    for row in range(9):
        for col in range(9):
            if(arr[row][col]=='.'):
                l[0]=row
                l[1]=col
                return True
    return False

def check_horizontal(arr,row,num):
    for i in range(9):
        if(arr[row][i] == num):
            return False
    return True

def check_vertical(arr,col,num):
    for i in range(9):
        if(arr[i][col] == num):
            return False
    return True

def check_group(arr,row,col,num):
    row=row-row%3
    col=col-col%3
    for i in range(3):
        for j in range(3):
            if(arr[i+row][j+col] == num):
                return False
    return True

def check_safe(arr,row,col,num):
    if(check_horizontal(arr,row,num) and check_vertical(arr,col,num) and check_group(arr,row,col,num)):
        return True
    else:
        return False
        
def solve_puzzle(arr):
    ind=[0,0]
    if(not has_empty(arr,ind)):
        return True
    row=ind[0]
    col=ind[1]
    for num in range(1,10):
        if(check_safe(arr,row,col,num)):
            arr[row][col]=num
            if(solve_puzzle(arr)):
                return True
            arr[row][col] = '.'

    return False

if __name__=="__main__":
    grid,x=puzzles.get_puzzle()
    print("\nPuzzle #{}:\n".format(x+1))
    display_grid(grid)
    print("\nSolution :\n")
    start = time.time()
    if(solve_puzzle(grid)):
        display_grid(grid)
        print("\n(Time taken to solve: {} secs)".format(time.time()-start))
    else:
        print ("No solution exists")
