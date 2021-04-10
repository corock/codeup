input_data = int(input())

for i in range(1, input_data + 1):
    if i % 3 == 0:
        continue
    print(i, end=" ")
