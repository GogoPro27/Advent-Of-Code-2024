from read import read_file


def main():
    lines = read_file("./puzzle_input.txt")
    line = [line.strip() for line in lines][0]
    # print(line)
    array = map(int,[c for c in line])
    blocks_array = []
    even = True
    id_ctr = 0
    for num in array:
        if even:
            for i in range(num):
                blocks_array.append(id_ctr)
            id_ctr+=1
            even = False
        else:
            for i in range(num):
                blocks_array.append(".")
            even = True
    # print("".join(map(str,array)))
    # print("".join(map(str,blocks_array)))

    for i in range(len(blocks_array)-1):
        if blocks_array[i]!=".":continue
        for j in range(len(blocks_array) - 1, i, -1):
            if i==j:continue
            if blocks_array[j] == ".": continue
            else:
                print(i,j)
                blocks_array[i],blocks_array[j] = blocks_array[j],blocks_array[i]
                break

    # print("".join(map(str, blocks_array)))
    # print("0099811188827773336446555566..............")

    total_sum = 0
    for i in range(len(blocks_array)):
        total_sum+=i*int(blocks_array[i])
        if blocks_array[i+1] == ".":break
    print(total_sum)




if __name__ == "__main__":
    main()