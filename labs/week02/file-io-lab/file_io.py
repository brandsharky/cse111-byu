# Q1
def count_lines():
    """
    Returns the number of lines in `filename`.

    >>> count_lines('text.txt')
    3
    """
    with open("test_files/text.txt") as file:
        return len(file.readlines())


# Q2
def write_n_times(filename, text, n):
    with open(filename, 'w') as file:
        while n > 0:
            file.write(text + "\n")
            n -= 1


# Q4
def filter_lines(in_file, out_file, filter):
    with open(in_file, "r") as input_file:
        with open(out_file, "w") as output_file:
            for line in input_file:
                if filter in line:
                    output_file.write(f"{line}\n")


# Q5
def copy_file(input, output):
    """Print each line from input with the line number and a colon prepended,
    then write that line to the output file.

    >>> copy_file('text.txt', 'output.txt')
    1: They say you should never eat dirt.
    2: It's not nearly as good as an onion.
    3: It's not as good as the CS pun on my shirt.
    """

    i = 1

    with open(input, "r") as input:
        with open(output, "w") as output:
            for line in input:
                print(f"{i}: {line}", end="")
                output.write(f"{i}: {line}")
                i += 1


# Q6
def reverse_lines(input, output):
    with open(input, "r") as input_file:
        lines = input_file.readlines()

    lines.reverse()

    with open(output, "w") as output_file:
        for line in lines:
            output_file.write(line)


# Q7
def merge_files(in_file1, in_file2, out_file):
    with open(in_file1, "r") as input1:
        with open(in_file2, "r") as input2:
            with open(out_file, "w") as output_file:

                lines1 = input1.readlines()
                lines2 = input2.readlines()

                i = 0

                while i < len(lines1) or i < len(lines2):
                    if i < len(lines1):
                        output_file.write(lines1[i])

                    if i < len(lines2):
                        output_file.write(lines2[i])

                    i += 1





if __name__ == "__main__":
    print(count_lines())
    # write_n_times("test_files/ntimes.txt", 'Hello!', 5)
    # filter_lines("test_files/in.txt", "text_files/out.txt", 'no')
    # copy_file("test_files/input.txt", "test_files/output.txt")