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

def similarity_score(l1:list,l2:list):
    my_dic = {}
    score = 0
    for i in l1:
        my_dic[i] = 0
        for j in l2:
            if i==j:
                my_dic[i]+=1
        score+= i * my_dic[i]
    return score


def main():
    lines = read_file("lists.txt")
    l1,l2 = process_lines(lines)
    score = similarity_score(l1,l2)
    print(score)




if __name__ == "__main__":
    main()
