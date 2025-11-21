from SinhVien import SinhVien

class QuanLySinhVien:
    listSinhVien = []

    def generateID(self):
        maxId = 1
        if (self.soluongSinhVien() > 0):
            maxId = self.listSinhVien[0].getId()
            for sv in self.listSinhVien:
                if (maxId < sv.getId()):
                    maxId = sv.getId()
            maxId = maxId + 1
        return maxId

    def soluongSinhVien(self):
        return len(self.listSinhVien)

    def nhapSinhVien(self):
        svId = self.generateID()
        name = input("Nhap ten sinh vien: ")
        sex = input("Nhap gioi tinh sinh vien: ")
        major = input("Nhap chuyen nganh cua sinh vien: ")
        diemTB = float(input("Nhap diem cua sinh vien: "))
        sv = SinhVien(svId, name, sex, major, diemTB)
        sv.setHocLuc()
        self.listSinhVien.append(sv)

    def updateSinhVien(self, ID):
        sv:SinhVien = self.findByID(ID)
        if (sv != None):
            name = input("Nhap ten sinh vien: ")
            sex = input("Nhap gioi tinh sinh vien: ")
            major = input("Nhap chuyen nganh cua sinh vien: ")
            diemTB = float(input("Nhap diem cua sinh vien: "))
            sv.name = name
            sv.sex = sex
            sv.major = major
            sv.diemTB = diemTB
            sv.setHocLuc()
        else:
            print(f"Sinh vien co ID = {ID} khong ton tai.")

    def sortByID(self):
        self.listSinhVien.sort(key=lambda x: x.getId(), reverse=False)

    def sortByName(self):
        self.listSinhVien.sort(key=lambda x: x.getName(), reverse=False)

    def sortByDiemTB(self):
        self.listSinhVien.sort(key=lambda x: x.getDiemTB(), reverse=False)

    def findByID(self, ID):
        searchResult = None
        if (self.soluongSinhVien() > 0):
            for sv in self.listSinhVien:
                if (sv.getId() == ID):
                    searchResult = sv
        return searchResult

    def findByName(self, keyword):
        listSV = []
        if (self.soluongSinhVien() > 0):
            for sv in self.listSinhVien:
                if (keyword.upper() in sv.getName().upper()):
                    listSV.append(sv)
        return listSV

    def deleteById(self, ID):
        isDeleted = False
        sv = self.findByID(ID)
        if (sv != None):
            self.listSinhVien.remove(sv)
            isDeleted = True
        return isDeleted

    def xepLoaiHocLuc(self, sv:SinhVien):
        if (sv.diemTB >= 8):
            sv.__hocLuc = "Giỏi"
        elif (sv.diemTB >= 6.5):
            sv.__hocLuc = "Khá"
        elif (sv.diemTB >= 5):
            sv.__hocLuc = "Trung bình"
        else:
            sv.__hocLuc = "Yếu"

    def showSinhVien(self, listSV):
        print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<10} {:<10}".format("ID", "Name", "Sex", "Major", "Diem TB", "Hoc luc"))
        if (listSV.__len__() > 0):
            for sv in listSV:
                print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<10} {:<10}".format(sv.getId(), sv.getName(), sv.getSex(), sv.getMajor(), sv.getDiemTB(), sv.getHocLuc()))
        print("\n")

    def getListSinhVien(self):
        return self.listSinhVien