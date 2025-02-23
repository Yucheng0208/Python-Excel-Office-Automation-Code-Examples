total = 0
for i in range(40, 68):
    if i % 2 != 0:
        print(i, end=" ")
        total += i
print("\n總和:", total)