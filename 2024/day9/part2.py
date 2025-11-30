from read import read_file

def compress_blocks(array):
    """Convert a character array into a list of (char, count) blocks."""
    if not array:
        return []
    blocks = []
    current_char = array[0]
    count = 1
    for ch in array[1:]:
        if ch == current_char:
            count += 1
        else:
            blocks.append((current_char, count))
            current_char = ch
            count = 1
    blocks.append((current_char, count))
    return blocks

def expand_blocks(blocks):
    """Convert a list of (char, count) blocks back into a character array."""
    result = []
    for ch, cnt in blocks:
        result.extend([ch]*cnt)
    return result

def main():
    lines = read_file("./puzzle_input.txt")
    line = [line.strip() for line in lines][0]
    array = list(map(int, line))
    blocks_array = []

    # Build initial blocks_array of digits and '.' according to input pattern
    even = True
    id_ctr = 0
    for num in array:
        if even:
            # number block
            for _ in range(num):
                blocks_array.append(str(id_ctr))
            id_ctr += 1
            even = False
        else:
            # dot block
            for _ in range(num):
                blocks_array.append(".")
            even = True

    # Convert to blocks
    blocks = compress_blocks(blocks_array)

    # Keep rearranging until no more changes
    changed = True
    while changed:
        changed = False
        # Iterate over dot blocks from left to right
        i = 0
        while i < len(blocks):
            char_i, length_i = blocks[i]
            if char_i == '.':
                # Try to find a suitable number block from the end
                j = len(blocks) - 1
                while j > i:
                    char_j, length_j = blocks[j]
                    if char_j == '.' or char_j == '.':
                        j -= 1
                        continue
                    # We found a number block at j
                    # If dot block i can fit this number block:
                    if length_i >= length_j:
                        # We'll rearrange blocks:
                        # The idea:
                        # 1) Replace part of the dot block i with the number block j.
                        # 2) The block j turns into dots of equal length.
                        # 3) If there's leftover dots, they stay after the replaced number block.

                        # Remove blocks i and j
                        left_part = blocks[:i]
                        right_part = blocks[j+1:]
                        middle_part = blocks[i+1:j]

                        # i-th block: '.' replaced by number block char_j of length_j
                        # plus leftover dots if length_i > length_j
                        new_blocks = []
                        new_blocks.extend(left_part)
                        new_blocks.append((char_j, length_j))  # replaced portion

                        leftover = length_i - length_j
                        if leftover > 0:
                            new_blocks.append(('.', leftover))

                        # middle remains the same
                        new_blocks.extend(middle_part)

                        # j-th block: replaced by dots of length_j
                        new_blocks.append(('.', length_j))

                        new_blocks.extend(right_part)

                        blocks = new_blocks
                        changed = True
                        # After rearranging, start from the beginning to ensure all rearrangements occur
                        break
                    j -= 1
                if changed:
                    # Break out to restart from beginning after a successful change
                    break
            i += 1

    # After no more changes, we have the final arrangement
    final_array = expand_blocks(blocks)
    # print("".join(final_array))

    # Calculate total_sum
    total_sum = 0
    for idx, val in enumerate(final_array):
        if val == ".":
            continue
        total_sum += idx * int(val)
    print(total_sum)


if __name__ == "__main__":
    main()