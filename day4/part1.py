from numpy.matrixlib.defmatrix import matrix

from read import read_file


def checkWord(word:str):
    return word=="XMAS" or word[::-1]=="XMAS"

def process_matrix (matrix:list[str]):
    count = 0
    len_xmas = len("XMAS")
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[0])):
            on=matrix[i][j]
            if on == 'M' or on=='A' or on=='.':
                continue
            if (j+len_xmas)<=len(matrix[0]):
                word = matrix[i][j:j+len_xmas]
                count+=checkWord(word)
            if (i+len_xmas)<=len(matrix):
                word = "".join([matrix[i+k][j]for k in range(0,len_xmas)])
                count+=checkWord(word)
            if (j+len_xmas)<=len(matrix[0]) and (i+len_xmas)<=len(matrix):
                word = "".join([matrix[i + k][j + k] for k in range(0, len_xmas)])
                count += checkWord(word)
            if (j + len_xmas) <= len(matrix[0]) and (i - len_xmas) >= -1:
                word = "".join([matrix[i - k][j + k] for k in range(0, len_xmas)])
                count += checkWord(word)
    return count



def main():
    lines = read_file("./puzzle_input.txt")
    lines = [line.strip() for line in lines]
    # [print(line) for line in lines]
    count = process_matrix(lines)
    print(count)




if __name__ == "__main__":
    main()