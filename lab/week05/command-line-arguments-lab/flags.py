import sys



def print_args(args):
    for arg in args:
        print(arg)


def is_flag(args):
    valid_flags = ["-p", "-i", "-h", "-w", "-r"]
    return len(args) > 1 and args[1] in valid_flags


def flags(args):
    flag = args[1]
    if flag == "-p":
        print_args(args[2:])
    elif flag == "-i":
        print("Hello World")
    elif flag == "-h":
        print("Valid flags:")
        print("-p : prints out all the command line arguments after the -p")
        print("-i : prints \"Hello World\"")
        print("-h : prints out a help command")
    elif flag == "-w":
        if len(args) < 4:
            print("No Content Provided")
        else:
            filename = args[2]
            content = args[3:]
            with open(filename, "w") as f:
                for line in content:
                    f.write(line + "\n")
    elif flag == "-r":
        filename = args[2]
        with open(filename, "r") as f:
            for line in f:
                print(line, end="")


def main():
    args = sys.argv
    if is_flag(args):
        flags(args)
    else:
        print_args(args)





if __name__ == "__main__":
    main()