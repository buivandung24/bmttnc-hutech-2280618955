from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()
while (1 == 1):
    print("\nCHUONG TRINH QUAN LY SINH VIEN")
    print("*************************MENU**************************")
    print("**  1. Them sinh vien.                             **")
    print("**  2. Cap nhat thong tin sinh vien boi ID.        **")
    print("**  3. Xoa sinh vien boi ID.                       **")
    print("**  4. Tim kiem sinh vien theo ten.                **")
    print("**  5. Sap xep sinh vien theo diem trung binh.     **")
    print("**  6. Sap xep sinh vien theo ten chuyen nganh.    **")
    print("**  7. Hien thi danh sach sinh vien.              **")
    print("**  0. Thoat                                        **")
    print("*******************************************************")

    key = int(input("Nhap tuy chon: "))
    if (key == 1):
        print("\n1. Them sinh vien.")
        qlsv.nhapSinhVien()
        print("\nThem sinh vien thanh cong!")
    elif (key == 2):
        print("\n2. Cap nhat thong tin sinh vien.")
        ID = int(input("Nhap ID: "))
        qlsv.updateSinhVien(ID)
    elif (key == 3):
        print("\n3. Xoa sinh vien.")
        ID = int(input("Nhap ID: "))
        if (qlsv.deleteById(ID)):
            print("\nSinh vien co ID = ", ID, " da bi xoa.")
        else:
            print("\nSinh vien co ID = ", ID, " khong ton tai.")
    elif (key == 4):
        print("\n4. Tim kiem sinh vien theo ten.")
        keyword = input("Nhap ten sinh vien can tim: ")
        searchResult = qlsv.findByName(keyword)
        qlsv.showSinhVien(searchResult)
    elif (key == 5):
        print("\n5. Sap xep sinh vien theo diem trung binh.")
        qlsv.sortByDiemTB()
        qlsv.showSinhVien(qlsv.getListSinhVien())
    elif (key == 6):
        print("\n6. Sap xep sinh vien theo ten chuyen nganh.")
        qlsv.sortByName()
        qlsv.showSinhVien(qlsv.getListSinhVien())
    elif (key == 7):
        print("\n7. Hien thi danh sach sinh vien.")
        qlsv.showSinhVien(qlsv.getListSinhVien())
    elif (key == 0):
        print("\n0. Thoat chuong trinh.")
        break