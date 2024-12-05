from numpy.polynomial.laguerre import laggrid3d

from read import read_file

def get_dic(rules:list[str]):
    my_dic = {}
    for rule in rules:
        n1,n2 = map(int,rule.split("|"))
        if n2 not in my_dic.keys():
            my_dic[n2] = []
        my_dic[n2].append(n1)
    return my_dic

def correct(nums:list[int],dic:dict[int,list[int]])->int:
    for i in range(0,len(nums)-1):
        if nums[i] in dic.keys():
            forbidden_nums = dic[nums[i]]
            if any([(nums[j] in forbidden_nums) for j in range(i+1,len(nums))]):
                return False
    return True


def correct_line(nums:list[int],dic:dict[int,list[int]]):
    i = 0
    #75,97,47,61,53 becomes 97,75,47,61,53.
    while i < len(nums)-1:
        for j in range(i+1,len(nums)):
            if nums[i] in dic.keys():
                if nums[j] in dic[nums[i]]:
                    tmp = nums[j]
                    tmp_list = nums[i:j]
                    nums[i+1:j+1] = tmp_list
                    nums[i] = tmp
                    i=0
        i+=1
    return nums

def main():
    lines = read_file("./puzzle_input.txt")
    lines = [line.strip() for line in lines]
    empty_line_idx = [i for i in range(0,len(lines)) if lines[i]==''][0]
    part1 = lines[:empty_line_idx]
    part2 = lines[empty_line_idx+1:]

    my_dic = get_dic(part1)
    sum = 0
    for update in part2:
        nums = list(map(int, update.split(",")))
        if not correct(nums,my_dic):
            new_nums = correct_line(nums,my_dic)
            # print(new_nums)
            sum+=nums[len(nums)//2]
    print(sum)







if __name__ == "__main__":
    main()