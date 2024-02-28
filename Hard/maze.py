import curses
from curses import wrapper
import queue
import time


maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", " ", " ", "#", "#", " ", "#", " ", "#"],
    ["#", "#", " ", "#", " ", " ", " ", " ", "#", "#"],
    ["#", " ", " ", " ", " ", "#", " ", " ", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", "#", " ", "#"],
    ["#", " ", " ", " ", "#", " ", " ", " ", " ", "#"],
    ["#", "#", "#", " ", "#", "#", " ", "#", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", "#", "#", "#", "#", " ", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#", "#"],
    ["#", " ", "#", " ", "#", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", " ", "#", " ", " ", " ", "#"],
    ["#", " ", " ", "#", " ", " ", " ", "#", "#", "#"],
    ["#", "#", " ", "#", " ", "#", " ", " ", " ", "#"],
    ["#", " ", " ", "#", " ", "#", "#", "#", "#", "#"],
    ["#", " ", "#", " ", " ", " ", " ", " ", "#", "#"],
    ["#", "#", " ", " ", "#", "#", "#", " ", " ", "#"],
    ["#", " ", " ", " ", "#", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "X", "#"],
]


def print_maze(maze, stdscr, path=[]):
    GREEN = curses.color_pair(1)
    RED = curses.color_pair(2)

    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if (i, j) in path:
                stdscr.addstr(i, j * 2, "X", RED)
            else:
                stdscr.addstr(i, j * 2, value, GREEN)


def find_path(maze, stdscr):
    start = "O"
    end = "X"
    start_position = find_start(maze, start)

    q = queue.Queue()
    q.put((start_position, [start_position]))

    visited = set()

    while not q.empty():
        current_position, path = q.get()
        row, col = current_position

        stdscr.clear()
        print_maze(maze, stdscr, path)

        time.sleep(0.1)
        stdscr.refresh()
        
        if maze[row][col] == end:
            return path

        neighbors = find_neighbor(maze, row, col)

        for neighbor in neighbors:
            if neighbor in visited:
                continue

            r, c = neighbor
            if maze[r][c] == "#":
                continue

            new_path = path + [neighbor]
            q.put((neighbor, new_path))
            visited.add(neighbor)


def find_neighbor(maze, row, col):
    neighbor = []


    if row < len(maze) - 1:  
        neighbor.append((row + 1, col))
    
    if row > 0:  
        neighbor.append((row - 1, col))

    if col > 0:  # LEFT
        neighbor.append((row, col - 1))

    if col < len(maze[0]) - 1:  
        neighbor.append((row, col + 1))

    return neighbor


def find_start(maze, start):
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return i, j
            else:
                continue

    return None


def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    find_path(maze, stdscr)
    
    stdscr.getch()

print(len(maze))
#wrapper(main)

start = "O"
end = "X"
start_position = find_start(maze, start)

q = queue.Queue()
q.put((start_position, [start_position]))

visited = set()


print(f"start position is: {start_position}")     #! This is to check for start point
row1, col1=start_position

nei=find_neighbor(maze, row1, col1)       #! Test find_neighbor below
print(f"neighbor is: {nei}")              #! This is to check for neighbor

current_position, path = q.get()

for neighbor in nei:                        #! test for loop
    r, c = neighbor
    if maze[r][c] == "#":
            continue 
          
    new_path=path+ [neighbor]
    print(f"Current path is :{path}, neighbor is :{neighbor}, new path is {new_path}")
    q.put((neighbor, new_path))
    
    
    
while not q.empty():
    current_position, path = q.get()
    row, col = current_position

    if maze[row][col] == end:
        break

    neighbors = find_neighbor(maze, row, col)

    for neighbor in neighbors:
        if neighbor in visited:
            continue

        r, c = neighbor
        if maze[r][c] == "#":
            continue

        new_path = path + [neighbor]
        q.put((neighbor, new_path))
        visited.add(neighbor)
