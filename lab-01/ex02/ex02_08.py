values = input("Nhập dãy số nhị phân 4 chữ số, cách nhau bằng dấu phẩy: ")
numbers = [x for x in values.split(',')]
result = []
for n in numbers:
    decimal = int(n, 2)
    if decimal % 5 == 0:
        result.append(n)
print(','.join(result))