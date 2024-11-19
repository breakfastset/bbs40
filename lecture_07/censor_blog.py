
def read_blog():
    """Read all lines of the file into a list of strings."""
    in_file = open("blog.txt", "r")
    lines = in_file.readlines()
    in_file.close()
    return lines


def censor(lines):
    """Replace all phrases containing vulgarity with sorry face."""
    for i in range(len(lines)):
        if "f***" in lines[i]:
            lines[i] = lines[i].replace("f***", "-_-\"")
    return lines


def save_cleaned_blog(lines):
    """Overwrite file with modified list of strings."""
    out_file = open("blog.txt", "w")

    for line in lines:
        out_file.write(line)

    out_file.close()


def main():
    """Start of program."""
    lines = read_blog()
    # censor the lines

    lines = censor(lines)

    print(lines)

    save_cleaned_blog(lines)


main()