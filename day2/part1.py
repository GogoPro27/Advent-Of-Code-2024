from day2.part2 import isSafe


def read_file(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
    return lines


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


def main():
    lines = read_file("./puzzle_input.txt")
    data = process_lines(lines)
    ctr = 0
    for report in data:
        if is_increasing(report) or is_decreasing(report): ctr+=1
    print(ctr)




if __name__ == "__main__":
    main()
