import sys
if __name__ == "__main__":
    print(f"reading numbers from {sys.argv[1]}!...")
    try:
        with open(sys.argv[1],'r') as f:
            total=0
            for line in f:
                total += int(line)
            print(total)
    except IndexError:
        print("missing file name:")

    except FileNotFoundError:
        print("f cannot open {sys.argv[1]!r}")
