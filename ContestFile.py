# with open("numbers.txt", "r", encoding="utf-8") as file:
#     numbers = map(int, file.read().split())
#     total = sum(numbers)
#
# with open("sum.txt", "w", encoding="utf-8") as file:
#     file.write(str(total))

# with open("data.bin", "rb") as file:
#     print(sum(file.read()))

with open("source.bin", "rb") as file:
    data = file.read()

with open("result.bin", "wb") as file:
    file.write(bytes(255 - x for x in data))

with open("values.txt", "r") as file:
    numbers = map(int, file.read().split())

with open("packed.bin", "wb") as file:
    file.write(bytes(x for x in numbers))