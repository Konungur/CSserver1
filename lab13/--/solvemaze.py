from maze_full import Maze

def main():
    maze = buildMaze( "mazefile.txt" )
    if maze.findPath() :
        print( "Path found...." )
        maze.draw()
    else :
        print( "Path not found...." )
        maze.draw()


def buildMaze( filename ):
    infile = open( filename, "r" )
    nrows, ncols = readValuePair( infile )
    maze = Maze( nrows, ncols )
    row, col = readValuePair( infile )
    maze.setStart( row, col )
    row, col = readValuePair( infile )
    maze.setExit( row, col )
    for row in range( nrows ) :
        line = infile.readline()
        for col in range( len(line) ) :
            if line[col] == "*" :
                maze.setWall( row, col )
    infile.close()
    return maze


def readValuePair( infile ):
    line = infile.readline()
    valA, valB = line.split()
    return int(valA), int(valB)

main()