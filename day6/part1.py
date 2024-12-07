from typing import List, Tuple

from missingno import matrix
from pyparsing import White

from read import read_file

def find_guard(field:list[str]):
    for i in range(len(field)):
        for j in range(len(field[0])):
            if field[i][j] != '#' and field[i][j] != '.':
                # print(field[i][j])
                return i,j
def get_obstacles(field: list[str]) -> list[tuple[int, int]]:
    return [(i, j) for i in range(len(field)) for j in range(len(field[0])) if field[i][j] == '#']

def make_move(field:list[str],visited:list[list[bool]]):
    x,y = find_guard(field)
    if field[x][y]=='^':
        direction = (-1,0)
    elif field[x][y]=='>':
        direction = (0,1)
    elif field[x][y]=='v':
        direction = (1,0)
    else:
        direction = (0,-1)

    next_direction = {"^":">",">":"v","v":"<","<":"^"}


    obstacles = get_obstacles(field)
    guard_char = field[x][y]
    field[x] = field[x].replace(guard_char,".")

    while (0 <= x < len(field) and 0 <= y < len(field[0])) and (x,y) not in obstacles:
        visited[x][y] = True
        x+=direction[0]
        y+=direction[1]

    if (x,y) in obstacles:
        x-=direction[0]
        y -= direction[1]
        if y != len(field[0]) - 1:
            field[x] = field[x][:y] + next_direction[guard_char] + field[x][y + 1:]
        else:
            field[x] = field[x][:y] + next_direction[guard_char]

    return field,visited


def main():
    lines = read_file("./test.txt")
    lines = [line.strip() for line in lines]
    visited_positions = [[False for char in line] for line in lines]
    # print(len(lines),len(lines[0]))
    # print(len(visited_positions),len(visited_positions[0]))

    while True:
        lines,visited_positions = make_move(lines,visited_positions)
        [print(line) for line in lines]
        print()
        is_in_row = [('^' in line or '>' in line or 'v' in line or '<' in line) for line in lines]
        if not any(is_in_row):
            break

    total_sum = 0
    for row in visited_positions:
        total_sum += sum(row)
    print(total_sum)




if __name__ == "__main__":
    main()