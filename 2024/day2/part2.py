from read import read_file

def process_lines(lines: list[str]):
    big_list = []
    for line in lines:
        line = line.replace("\n","")
        line = line.strip()
        numbers_list = [int(i) for i in line.split(" ")]
        big_list.append(numbers_list)
        assert len(numbers_list)>=2
    return big_list
def is_increasing(l):
    return all(l[i] < l[i+1] and 1 <= abs(l[i] - l[i+1]) <= 3 for i in range(len(l)-1))

def is_decreasing(l):
    return all(l[i] > l[i+1] and 1 <= abs(l[i] - l[i+1]) <= 3 for i in range(len(l)-1))

def isSafe(l, removed=False):
    if is_increasing(l) or is_decreasing(l):
        return True
    if removed:
        return False
    for i in range(len(l)):
        new_list = l[:i] + l[i+1:]
        if isSafe(new_list, True):
            return True
    return False

def main():
    lines = read_file("./puzzle_input.txt")
    data = process_lines(lines)

    ctr = 0
    for report in data:
        safe = isSafe(report)
        if safe: ctr+=1
    print(ctr)




if __name__ == "__main__":
    main()
