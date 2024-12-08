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
                        hashtag1 = (i-distance[0],j-distance[1])
                        hashtag2 = (p+distance[0],q+distance[1])
                        if in_bounds(hashtag1,lines) and not hashtag_matrix[hashtag1[0]][hashtag1[1]]:
                            ctr+=1
                            hashtag_matrix[hashtag1[0]][hashtag1[1]] = True
                        if in_bounds(hashtag2,lines) and not hashtag_matrix[hashtag2[0]][hashtag2[1]]:
                            ctr+=1
                            hashtag_matrix[hashtag2[0]][hashtag2[1]] = True
    print(ctr)
    [print(line) for line in lines]







if __name__ == "__main__":
    main()