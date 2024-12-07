from read import read_file


def generate_combinations(n):
    if n == 0:
        return []
    if n == 1:
        return ['*', '+','|']
    smaller_combinations = generate_combinations(n - 1)
    result = []
    for combo in smaller_combinations:
        result.append(combo + '*')
        result.append(combo + '+')
        result.append(combo + '|')
    return result

def mult(num):
    if num < 10:
        return 10
    return 10*mult(num/10)
def do_operation(a,b,operator):
    multiplication = mult(b)
    if operator == '+':
        return a+b
    elif operator=='*':
        return a*b
    else:
        return (multiplication*a)+b

def process_equation(test_value:int, numbers:list[int]):
    operators_combinations = generate_combinations(len(numbers)-1)

    for combination in operators_combinations:
        tmp= 0
        for i in range(len(numbers)-1):
           if i==0:
               tmp = do_operation(numbers[0],numbers[1],combination[i])
           else:
               tmp = do_operation(tmp,numbers[i+1],combination[i])
        if tmp == test_value:
            return test_value
    return 0

def process_line(line:str):
    line = line.strip()
    parts = line.split(":")
    number = int(parts[0])
    other_numbers = list(map(int,(parts[1].strip()).split(" ")))
    return number,other_numbers

def main():
    lines = read_file("./puzzle_input.txt")

    total_sum = 0
    for line in lines:
        test_num,other_nums = process_line(line)
        total_sum += process_equation(test_num,other_nums)

    print(total_sum)





if __name__ == "__main__":
    main()