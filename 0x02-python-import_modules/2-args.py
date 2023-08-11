#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv

    if len(argv) == 1:
        print("0 arguments.")
    else:
        print(len(argv) - 1, "argument:" if len(argv) == 2 else "arguments:")

        for index, value in enumerate(argv[1:], start=1):
            print(index, ":", value)
