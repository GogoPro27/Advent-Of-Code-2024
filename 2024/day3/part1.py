from read import read_file



def get_sum(line:str)->int:
    global n1,n2,inSequence,inNumber1,inNumber2,sum
    inSequence = False
    inNumber1,inNumber2 = False,False
    n1,n2 = 0,0
    sum=0

    global i
    i=0
    while i<len(line):
        curr = line[i]
        if not inSequence:
            mul = line[i:i + 4]
            if mul=='mul(':
                inSequence = True
                inNumber1 = True
                i+=4
                continue
        else: #in SEQUENCE
            if curr.isnumeric():
                if inNumber1:
                    n1 = n1*10 + int(curr)
                    if n1>999:
                        inSequence=False
                        inNumber1, inNumber2 = False, False
                        n1,n2 = 0,0
                elif inNumber2:
                    n2 = n2 * 10 + int(curr)
                    if n2 > 999:
                        inSequence = False
                        inNumber1, inNumber2 = False, False
                        n1, n2 = 0, 0
                else:
                    inSequence = False
                    inNumber1, inNumber2 = False, False
                    n1, n2 = 0, 0

            else:
                if curr==',':
                    if inNumber1:
                        inNumber1=False
                        inNumber2=True
                    else:
                        inSequence = False
                        inNumber1, inNumber2 = False, False
                        n1, n2 = 0, 0
                elif curr==')':
                    if inNumber2:
                        inNumber2=False
                        sum+=n1*n2
                        inSequence = False
                        n1, n2 = 0, 0
                    else:
                        inSequence = False
                        inNumber1, inNumber2 = False, False
                        n1, n2 = 0, 0
                else:
                    inSequence = False
                    inNumber1, inNumber2 = False, False
                    n1, n2 = 0, 0
        i+=1

    return sum





def main():
    lines = read_file("./puzzle_input.txt")
    sum = 0
    for line in lines:
        sub_sum = get_sum(line)
        sum+=sub_sum
    print(sum)


if __name__ == "__main__":
    main()
