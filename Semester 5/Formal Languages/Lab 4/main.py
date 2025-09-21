from scanner import Scanner


def main():
    scan = Scanner("p1.txt", "token.in")
    scan.scan_file()


if __name__ == "__main__":
    main()