from read import read_file


def in_bounds(coords,lines):
    return coords[0] in range(len(lines)) and coords[1] in range(len(lines[0]))

def main():
    lines = read_file("./puzzle_input.txt")
    lines = [line.strip() for line in lines]
    ctr = 0
    hashtag_matrix = [[False for char in line] for line in lines]
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            c1 = lines[i][j]
            if c1 in ".#":continue
            for p in range(i,len(lines)):
                for q in range(len(lines[0])):
                    if i==p and q<=j:continue

                    c2 = lines[p][q]
                    if c2 in ".#": continue
                    if c1 == c2:
                        distance = (p-i,q-j)
                        tmp_x = i
                        tmp_y = j
                        while tmp_x in range(len(lines)) and tmp_y in range(len(lines[0])):
                            if not hashtag_matrix[tmp_x][tmp_y]:
                                hashtag_matrix[tmp_x][tmp_y] = True
                                ctr+=1
                            tmp_x-=distance[0]
                            tmp_y-=distance[1]
                        tmp_x = p
                        tmp_y = q
                        while tmp_x in range(len(lines)) and tmp_y in range(len(lines[0])):
                            if not hashtag_matrix[tmp_x][tmp_y]:
                                hashtag_matrix[tmp_x][tmp_y] = True
                                ctr += 1
                            tmp_x += distance[0]
                            tmp_y += distance[1]


    print(ctr)







if __name__ == "__main__":
    main()