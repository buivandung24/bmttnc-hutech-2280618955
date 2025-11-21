class SinhVien:
    def __init__(self, id, name, sex, major, diemTB):
        self.__id = id
        self.name = name
        self.sex = sex
        self.major = major
        self.diemTB = diemTB
        self.__hocLuc = ""

    def getId(self):
        return self.__id

    def getName(self):
        return self.name

    def getSex(self):
        return self.sex

    def getMajor(self):
        return self.major

    def getDiemTB(self):
        return self.diemTB

    def setHocLuc(self):
        if self.diemTB >= 8:
            self.__hocLuc = "Giỏi"
        elif self.diemTB >= 6.5:
            self.__hocLuc = "Khá"
        elif self.diemTB >= 5:
            self.__hocLuc = "Trung bình"
        else:
            self.__hocLuc = "Yếu"

    def getHocLuc(self):
        return self.__hocLuc