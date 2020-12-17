def reader():
    with open ('data12.txt') as inputFile:
        tab = inputFile.read().splitlines()
        tab = [(x[0], x[1:]) for x in tab]
    return tab

def decide(x, facing, pos):
    dir, dis = x
    dis = int(dis)
    if dir == 'R' or dir == 'L':
        rotate = dis//90
        if dir == 'L':
            rotate = rotate*(-1)
        facing = abs((facing + rotate)%4)
    elif dir == 'N' or dir == 'S':
        if dir == 'S':
            dis = dis*(-1)
        pos[0] += dis
    elif dir == 'W' or dir == 'E':
        if dir == 'W':
            dis = dis*(-1)
        pos[1] += dis
    else:
        if facing == 0:
            pos[0] += dis
        elif facing == 1:
            pos[1] += dis
        elif facing == 2:
            pos[0] -= dis
        else:
            pos[1] -= dis 
    return pos, facing

def move(tab):
    pos = [0,0]
    facing = 1
    for x in tab:
        pos, facing = decide(x, facing, pos)
    return pos

def waypointDecide(x, waypointPos, shipPos):
    dir, dis = x
    dis = int(dis)
    if dir == 'R' or dir == 'L':
        rotate = dis//90
        if dir == 'L':
            rotate = rotate*(-1)
        if rotate == -1 or rotate == 3:
            tmp = waypointPos[0]
            waypointPos[0] = waypointPos[1]
            waypointPos[1] = -(tmp)
        elif rotate == 2 or rotate == -2:
            waypointPos[0] = -(waypointPos[0])
            waypointPos[1] = -(waypointPos[1])
        elif rotate == 1 or rotate == -3:
            tmp = waypointPos[0]
            waypointPos[0] = -(waypointPos[1])
            waypointPos[1] = tmp
    elif dir == 'N' or dir == 'S':
        if dir == 'S':
            dis = dis*(-1)
        waypointPos[0] += dis
    elif dir == 'W' or dir == 'E':
        if dir == 'W':
            dis = dis*(-1)
        waypointPos[1] += dis
    else:
        shipPos[0] += dis * waypointPos[0]
        shipPos[1] += dis * waypointPos[1]
    return waypointPos, shipPos

def waypointShip(tab):
    shipPos = [0, 0]
    waypointPos = [1, 10]
    for x in tab:
        waypointPos, shipPos = waypointDecide(x, waypointPos, shipPos)
    return shipPos
        
    
tab = reader()
#first
position = move(tab)
print(abs(position[0]) + abs(position[1]))
#second
secondPosition = waypointShip(tab)
print(abs(secondPosition[0]) + abs(secondPosition[1]))