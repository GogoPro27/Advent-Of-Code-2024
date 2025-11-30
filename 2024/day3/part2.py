from read import read_file

ALLOWED_SUM = True

def get_sum(line:str)->int:
    global ALLOWED_SUM
    in_sequence = False
    in_number1,in_number2 = False,False
    n1,n2 = 0,0
    line_sum=0
    global i
    i=0
    while i<len(line):
        curr = line[i]
        ##### don't() addition
        len_dont = len("don't()")
        if (i+len_dont) < len(line):
            dont = line[i:i+len_dont]
            if dont == "don't()":
                if in_sequence:
                    in_sequence = False
                    in_number1, in_number2 = False, False
                    n1, n2 = 0, 0
                i+=len_dont
                ALLOWED_SUM = False
                continue
        ##### do() addition
        len_do = len("do()")
        if (i + len_do) < len(line):
                do = line[i:i + len_do]
                if do == "do()":
                    if in_sequence:
                        in_sequence = False
                        in_number1, in_number2 = False, False
                        n1, n2 = 0, 0
                    i += len_do
                    ALLOWED_SUM = True
                    continue

        if not in_sequence:
            mul = line[i:i + 4]
            if mul=='mul(':
                in_sequence = True
                in_number1 = True
                i+=4
                continue
        else: #in SEQUENCE
            if curr.isnumeric():
                if in_number1:
                    n1 = n1*10 + int(curr)
                    if n1>999:
                        in_sequence=False
                        in_number1, in_number2 = False, False
                        n1,n2 = 0,0
                elif in_number2:
                    n2 = n2 * 10 + int(curr)
                    if n2 > 999:
                        in_sequence = False
                        in_number1, in_number2 = False, False
                        n1, n2 = 0, 0
                else:
                    in_sequence = False
                    in_number1, in_number2 = False, False
                    n1, n2 = 0, 0

            else:
                if curr==',':
                    if in_number1:
                        in_number1=False
                        in_number2=True
                    else:
                        in_sequence = False
                        in_number1, in_number2 = False, False
                        n1, n2 = 0, 0
                elif curr==')':
                    if in_number2:
                        in_number2=False
                        if ALLOWED_SUM:
                            line_sum+= n1 * n2
                        in_sequence = False
                        n1, n2 = 0, 0
                    else:
                        in_sequence = False
                        in_number1, in_number2 = False, False
                        n1, n2 = 0, 0
                else:
                    in_sequence = False
                    in_number1, in_number2 = False, False
                    n1, n2 = 0, 0
        i+=1

    return line_sum





def main():
    global ALLOWED_SUM
    lines = read_file("./puzzle_input.txt")
    sum = 0
    ALLOWED_SUM = True
    for line in lines:
        sub_sum = get_sum(line)
        sum+=sub_sum
    print(sum)


if __name__ == "__main__":
    main()
