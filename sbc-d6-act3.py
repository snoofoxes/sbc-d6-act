rows = 5
for i in range(rows, 0, -1):
    for j in range(0, i + 1):
        print("*", end="")
    print("\r")
print("*" + (" ") * (rows-1) + "*")
for i in range(2, rows + 2):
	print("*"*i)