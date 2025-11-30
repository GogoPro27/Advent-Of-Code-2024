from read import read_file
# - If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.

# - If the stone is engraved with a number that has an even number of digits,
# it is replaced by two stones. The left half of the digits are engraved on the new left stone,
# and the right half of the digits are engraved on the new right stone.
# (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)

# - If none of the other rules apply, the stone is replaced by a new stone;
# the old stone's number multiplied by 2024 is engraved on the new stone.

def blink(nums:list[int]):
    #0 1 2 3
    new_nums = []
    for num in nums:
        if num==0:
            new_nums.append(1)
        elif len(str(num))%2 == 0:
            left_half = int(str(num)[:len(str(num)) // 2])
            right_half = int(str(num)[len(str(num)) // 2:])
            new_nums.append(left_half)
            new_nums.append(right_half)
        else:
            new_nums.append(num*2024)
    return new_nums

def main():
    lines = read_file("./puzzle_input.txt")
    line = [line.strip() for line in lines][0]
    numbers = list(map(int,line.split(" ")))
    # [print(line) for line in lines]
    blinks = int(input("Enter num of blinks: "))
    # print(numbers)
    # print(blinks)
    for i in range(blinks):
        numbers = blink(numbers)
        print(i)
    # print(numbers)
    print(len(numbers))



if __name__ == "__main__":
    main()