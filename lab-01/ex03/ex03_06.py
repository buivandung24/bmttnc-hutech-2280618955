# Tạo một Dictionary mẫu
my_dict = {'name': 'Alice', 'age': 25, 'city': 'Hanoi'}

# Nhập key cần xóa
key = input("Nhập key cần xóa: ")

# Kiểm tra và xóa
if key in my_dict:
    del my_dict[key]
    print("Đã xóa thành công!")
else:
    print("Key không tồn tại!")

# In kết quả
print("Dictionary sau khi xóa:", my_dict)