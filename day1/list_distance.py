from read import read_file


def process_line(line:str):
    num1,num2 = "",""
    flag1,flag2 = True,False
    for char in line:
        if char.isnumeric():
            if flag1:
                num1 = num1+char
            elif flag2:
                num2 = num2+char
        else:
            if flag1:
                flag1=False
                flag2 = True
    return int(num1),int(num2)


def process_lines(lines:list):
    l1,l2 = [],[]
    for line in lines:
        n1,n2 = process_line(line)
        l1.append(n1)
        l2.append(n2)
    return l1,l2


def main():
    lines = read_file("lists.txt")
    l1,l2 = process_lines(lines)
    l1.sort()
    l2.sort()
    sum = 0
    for n1,n2 in zip(l1,l2):
        sum+= abs(n1-n2)
    print(sum)

if __name__ == "__main__":
    main()
