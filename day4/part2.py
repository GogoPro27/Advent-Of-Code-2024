from numpy.matrixlib.defmatrix import matrix

from read import read_file


def checkWord(word:str):
    return word=="MAS" or word[::-1]=="MAS"

def process_matrix (matrix:list[str]):
    count = 0
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[0])):
            on=matrix[i][j]
            if on != 'A':
                continue
            if i-1 >= 0 and i+1<len(matrix):
                if j-1>=0 and j+1<len(matrix[0]):
                    w1 = "".join([matrix[i+k][j+k] for k in range(-1,2)])
                    w2 = "".join([matrix[i+k][j-k] for k in range(-1,2)])
                    if checkWord(w1) and checkWord(w2):
                        count+=1

    return count



def main():
    lines = read_file("./puzzle_input.txt")
    lines = [line.strip() for line in lines]
    # [print(line) for line in lines]
    count = process_matrix(lines)
    print(count)




if __name__ == "__main__":
    main()