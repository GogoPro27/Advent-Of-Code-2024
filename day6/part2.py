import copy

from read import read_file

def find_guard(field:list[str]):
    for i in range(len(field)):
        for j in range(len(field[0])):
            if field[i][j] != '#' and field[i][j] != '.':
                # print(field[i][j])
                return i,j
def get_obstacles(field: list[str]) -> list[tuple[int, int]]:
    return [(i, j) for i in range(len(field)) for j in range(len(field[0])) if field[i][j] == '#']

def make_move2(field:list[str], visited:list[tuple[tuple[int, int] | str, ...]]):
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
        visit = tuple([(x,y),guard_char])
        visited.append(visit)
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
    lines = read_file("./puzzle_input.txt")
    lines = [line.strip() for line in lines]
    visited_positions = [[False for char in line] for line in lines]

    lines_tmp = copy.deepcopy(lines)
    while True:
        lines_tmp,visited_positions = make_move(lines_tmp,visited_positions)
        is_in_row = [('^' in line or '>' in line or 'v' in line or '<' in line) for line in lines_tmp]
        if not any(is_in_row):
            break


    ctr = 0
    iter = 0
    print(len(visited_positions))
    for i in range(len(visited_positions)):
        print(i)
        for j in range(len(visited_positions[0])):
            if not visited_positions[i][j]:continue
            if lines[i][j]!='.':continue
            iter+=1
            lines_tmp = copy.deepcopy(lines)
            visited = []

            if j != len(lines_tmp[0]) - 1:
                lines_tmp[i] = lines_tmp[i][:j] + "#" + lines_tmp[i][j+1:]
            else:
                lines_tmp[i] = lines_tmp[i][:j] + "#"

            while True:
                lines_tmp, visited = make_move2(lines_tmp, visited)
                if len(visited) != len(set(visited)):
                    ctr += 1
                    break
                is_in_row = [('^' in line or '>' in line or 'v' in line or '<' in line) for line in lines_tmp]
                if not any(is_in_row):
                    break
    print()
    print(ctr)
    print(iter)








if __name__ == "__main__":
    main()