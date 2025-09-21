from scanner import Scanner


def main():
    scan = Scanner("p1err.txt", "token.in")
    scan.scan_file()


if __name__ == "__main__":
    main()