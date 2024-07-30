# Absolute path: Specifies a complete path from the root directory (e.g., /home/user/file.txt).
# Relative path: Specifies a path relative to the current working directory (e.g., ../file.txt).

# Relative to sub folders in current folder
with open("./sub_folder/file.txt") as file:
    content = file.read()

print(content)

# Relative for upper folder from current folder (use ../../ for more up levels)
with open("../024-intermediate-snake-game-improved/highscore.txt") as file:
    content = file.read()

print(content)
