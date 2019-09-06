import random , sys
world = []
rows = 0
cols = 0

def new_world(r,c):

    global world, rows, cols
    # make the world size
    rows = r
    cols = c
    world = [[0 for x in range(c)]for y in range(r)]


def knight_position():
    pass


def possibleMove(current_pos):
    # take current position
    # list all possible move knight can move
    listOfPossibleMove = [
        [current_pos[0] + 1, current_pos[1] + 2],
        [current_pos[0] + 1, current_pos[1] - 2],
        [current_pos[0] + 2, current_pos[1] + 1],
        [current_pos[0] + 2, current_pos[1] - 1],
        [current_pos[0] - 1, current_pos[1] + 2],
        [current_pos[0] - 1, current_pos[1] - 2],
        [current_pos[0] - 2, current_pos[1] + 1],
        [current_pos[0] - 2, current_pos[1] - 1],
                          ]
    return listOfPossibleMove


def remove_out_of_world_move(list1):
    global rows, cols, world
    # take list of possible move
    # remove position out of world
    listAfterRemove = []
    listAfterMoveCheck = []
    for i in list1:
        if (0 <= i[0] < cols) and (0 <= i[1] < rows):
            listAfterRemove.append(i)
    for j in listAfterRemove:
        if world [j[0]] [j[1]] == 0:
            listAfterMoveCheck.append(j)

    return listAfterMoveCheck


def knight_move(legalMove):
    # legalMove
    next_pos = random.choice(legalMove)
    return next_pos



def print_board():
    global world
    print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                     for row in world]))


def knightsTour(r, c, att):
    current_att = 0
    currentPos = []
    msg = 'Fail'

    while current_att < att:
        new_world(r, c)
        start_pos = [0, 0]
        current_pos = start_pos
        move = 1

        while currentPos is not[]:
            world[current_pos[0]][current_pos[1]] = move
            legalMove = remove_out_of_world_move(possibleMove(current_pos))
            if not legalMove:
                break
            current_pos = knight_move(legalMove)
            move += 1

        if move == rows*cols:
            msg = 'success'
            break
        current_att += 1
    print(msg)
    print_board()



if __name__ == '__main__':
    knightsTour(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]))
    # knightsTour(6,6,1000000)
