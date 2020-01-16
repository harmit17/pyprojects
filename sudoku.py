#assume board is completely filled
def solve(bo):

    #recursive approach
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col =find

    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False

def valid(bo, num, pos):  #3 parameters board, number which we inserted and position which is come from find empty

    #check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i: #IGNORE THE position where we just inserted and check where the number is available in row
            return False      #pos[0] means return value of find_empty which is i and j here 0 means i and pos[1] != i means do not check where number is inserted

    #check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range( box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True

def print_board(bo):

    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
           if j % 3 == 0 and j != 0:
               print(" | ",end="")      #print pipe and stay on the same line

           if j == 8:
               print(bo[i][j])
           else:                        #printing numbers, putting space and stay on the same line
               print(str(bo[i][j]) + " " , end="") #end="" stay on the same line


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i,j)        #return row and column

    return None
