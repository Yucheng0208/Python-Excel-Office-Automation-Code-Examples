def print_stars(rows):
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "* " * i)

print_stars(7)