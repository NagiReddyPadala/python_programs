import os
def print_last_lines(file, no_of_lines):
    with open(file, 'r') as f:
        f.seek(0, os.SEEK_END)
        cursor_position = f.tell() - 1
        last_lines = []
        line = ""
        lines = 0
        while cursor_position >= 0 and no_of_lines > lines:
            f.seek(cursor_position)
            char = f.read(1)
            if char == "\n":
                last_lines.append(line[::-1])
                cursor_position -= 2
                line = ""
                lines += 1
                continue
            line += char
            cursor_position -= 1
        for line in reversed(last_lines):
            print(line)
print_last_lines("lines.txt", 5)
