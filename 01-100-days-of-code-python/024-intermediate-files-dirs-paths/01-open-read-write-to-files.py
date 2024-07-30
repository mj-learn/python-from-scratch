# Some userful modes
# "r"  - Read (default).
# "w"  - Write (truncate).
# "x"  - Write or fail if the file already exists.
# "a"  - Append.
# "w+" - Read and write (truncate).
# "r+" - Read and write from the start.
# "a+" - Read and write from the end.
# "t"  - Text mode (default).
# "b"  - Binary mode.

some_file = open("01-file.txt")
content_1 = some_file.read()
some_file.close()
print(content_1)

# Correct way of open files
with open("01-new_file.txt", "a+") as file:
    file.write("\nHello from python")
