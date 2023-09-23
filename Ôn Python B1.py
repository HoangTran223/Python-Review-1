print("Buổi ôn đầu tiên, Python tự xuống dòng")
print(3*"In 3 lần và xuống dòng\n")
print("Kết thúc bằng chấm than","thay đổi dấu phân tách giữa các đtuong", sep = " => ", end = '!')
age = 18
print("\nDấu cách tự bổ sung giữa các phần", age)


def hello():
    print ("Gọi hàm")
if __name__ == "__main__":              # gọi tên hàm trong bthuc thì có __Name__
    hello()


khaibao = "14"
print(type(khaibao))                    # Python tự động xđịnh kiểu dữ liệu
khaibao = int(khaibao)
print(type(khaibao))                    # Ép kiểu 


# Biến cục bộ chỉ thay đổi trong hàm, ngoài hàm là mất
# Cách thay đổi, truy xuất biến toàn cục: sdung global
biencucbo="Biencucbo"
def BIENCUCBO():
    global biencucbo
    biencucbo = "Thay đổi Biencucbo"
    print(biencucbo)
print(biencucbo)         # In ra Biencucbo
BIENCUCBO()              # In ra Thay đổi Biencucbo



# CHUỖI:

# Biểu thị chuỗi trên nhiều dòng:
print(""" Biểu thị
trên nhiều dòng, 
hoặc dùng dấu ''' """)

# Nối chuỗi: 
print("Hello" + "World")      # In ra HelloWorld

# Cắt chuỗi:
catchuoi="CATCHUOI"
print( catchuoi[1:5] )          # In ra ATCH
print( catchuoi[-5:-2])         # In ra CHU



# HÀM INPUT: để bắt lại gtri nhập, ta sdung 1 biến lưu 
# Đầu ra của hàm Input luôn là chuỗi kí tự
InputFunction= input("Hãy nhập số thứ tự: ")
print(InputFunction)



# Kiểm tra kiểu dữ liệu:
kiemtradl  = 16 + 24j
print(isinstance(kiemtradl, complex))      # In ra True


# If-else : các câu lệnh trong cùng khối lệnh phải thụt 1 khoảng như nhau



# DANH SÁCH (LIST):

[int(x) for x in input("Nhập các phần tử là số nguyên của danh sách trên một dòng: ").split()]
list(map(float, input("Nhập các phần tử là số của danh sách trên một dòng: ").split()))

# Khai báo:
khaibaolist1= [300,200,[10,50,"List có thể khai báo chồng nhau"]]
khaibaolist2  = list([100,200,"Cách khai báo khác", [10,20,40]])
print(khaibaolist1[2][1])                  # In ra 50
print(khaibaolist2[-1][-3])                # In ra 10


# Lấy 1 dsach con: list[start: end: step]
dscon = khaibaolist1[1:4:2]       # In ra [200]
                                  # Step > 0: cắt từ đầu ds, < 0 cắt cuối ds

# Gán:
gan = [10,20,30,40]
gan[0:3] = [60, 50]
print(gan)                        # In ra [60,50,40]

# Thêm, xóa, tìm ptu, sắp xếp, đảo dsach, sao chép, đếm số ptu:
danhsach = [1,2,3,4,5,6,7]
danhsach.insert(3, 3.5)         # (vtri, gtri)
danhsach.extend([8,9,10])       # Thêm 1 list dsach vào cuối dsach
danhsach.append(99)             # Thêm vị trí đầu tiên
print(danhsach)
danhsach.remove(6)              # Xóa 1 lần xuất hiện đầu tiên của phần tử
danhsach.pop(2)                 # Xóa ptu tại vị trí 2
del danhsach[2:5]               # Xóa ptu từ vtri 2-4

print(100 not in danhsach)      # In ra True 

print(danhsach.index(7,1,4))        # Trả về lần xuất hiện đầu tiên của 7 trong ds đầu, [1,4] là giới hạn tìm kiếm
                                    # Nếu ko có 7 trong [1,4] in ra ValueError


sapxepds = [ "h", "ha", "haa", "haaa"]
def length(a):
    return len(a)
sapxepds.sort(reverse= True, key = length)              
print(sapxepds)                                         # Sắp xếp theo thứ tự của hàm, reverse sẽ theo thứ tự giảm dần
print(max(sapxepds))                                    # In ra haaa
print(sapxepds.count('a'))                              # Số lần xuất hiện kí tự 'a' , in ra 0
copyds = sapxepds.copy()


hamktra  = [0, 1, True]
print(all(hamktra))                                     # In ra False
print(any(hamktra))                                     # In ra True



# CHUỖI KÍ TỰ:

# Thay đổi kí tự: chuỗi kí tự có tính bất biến, ko tdoi như ds được, chỉ có cách:
tdoikitu = "Thay đổi kí tự"
tdoikitu = tdoikitu.replace('Thay đổi', 'THAY ĐỔI')
tdoitructiep = tdoikitu[:4] + " đổi trực tiếp"
# Ko xóa được kí tự, chỉ sdung cách trên để xóa


chuyendoichuoi="Chuyển Đổi Kí Tự"
chuyeninhoa = chuyendoichuoi.upper()
chuyeninthuong = chuyendoichuoi.lower()


# Chuẩn hóa chuỗi: chỉ loại bỏ các kí tự đầu, cuối, kí tự giữa ko thay đổi
chuanhoachuoi1 = "##**## Chuẩn hóa chuỗi **##**"
chuanhoaphai = chuanhoachuoi1.rstrip('*')
chuanhoatrai  = chuanhoachuoi1.lstrip('#')
chuanhoachuoi2 = "www.example.com"
chuanhoa = chuanhoachuoi2.strip('cmow')               # Sẽ loại bỏ từ w-o-c, ko loại m vì m ở giữa
print(chuanhoa)
print(chuanhoaphai)
print(chuanhoatrai)


# Tách chuỗi: trả về 1 dsach con
tachchuoi = "Tách chuỗi 1 2 3"
print(tachchuoi.split(' ', 3))                        # Tách từ phải - trái
print(tachchuoi.rsplit(',', 2))                       # Ko có dấu , trong chuỗi thì nó giữ nguyên

noichuoi1 = "abcd"
noichuoi2 = "1234"
noichuoi = noichuoi1.join(noichuoi2)                  # In ra 1abcd2abcd3abcd4abcd
print(noichuoi)



# ĐỊNH DẠNG CHUỖI:

# Định dạng với format:
print ("Ví dụ dùng {0:^} là phân tách hàng nghìn,{1:b} là định dạng số nhị phân".format(123, 456, 789))
print ("Để căn lề trái, ta dùng {0:<6}, còn căn lề phải dùng {1:>10}, căn giữa là {2:^8}".format('A','B','C'))

# Định dạng với f-string: cho phép ttoan trực tiếp trong f""
def cong(a):
    return pow(a,4)
print( f"{cong(6)*4}")
print( f"In ra ký tự đặc biệt, ví dụ như: \'{'dấu phẩy trên'}\', hay {{dấu ngoặc}} ")


# VÒNG LẶP:
def ktraSNT(a):
    dem = 1
    for i in range(1,a):
        if a%i == 0:
            dem += 1
            break
    if ( dem == 1):
        return 1
    else:
        return 0
print( ktraSNT(131) )                   # In ra 0

for i in range (5):
    if(i % 2 == 0):
        continue
    print(i)                            # In ra 1,3


# ĐỐI SỐ: 
def doiso(*a):                          # Ko biết số lượng đối số truyền trong hàm, sdung *
    for i in a:
        print(i)
doiso(5,9,12)                           # In ra 5,9,12


# HÀM LAMBDA:
dsachham1 = [1,2,3,4,5,6,7,8,9,10]
print(list(filter(lambda x: (x**2-1)%4==0, dsachham1)))              # Hàm filter lọc ra các phần tử trong ds 
                                                                     # theo đkien, trả về 1 ds mới

print(list(map(lambda x: pow(x,4),dsachham1)))                       # Hàm map biến đổi các phần tử của ds theo hàm, trả về 1 ds mới

dsachham2 = [[1,2,3], [4,5,6]]
print(list(map (lambda x: sum(x), dsachham2)))



# TUPLE:
hamtuple = tuple(("là tập dlieu hỗn hợp",1,"thao tác cơ bản, nối, tìm kiếm ttu dsach",[1,2,3],"khác cách tạo, sửa, xóa,..." )) # Phải có nhiều () 
print(hamtuple)
hamtuplemoi = list(hamtuple)
hamtuplemoi[4] = "Ép kiểu để thay đổi gtri, xóa"
print(hamtuplemoi)

# Packing và Unpacking:

*packing1, = 1, 2                           # Phải có dấu , ở sau
m, n, *p = (1,2,3,4)                        # Chia thành 1, 2, (3,4)
*m1, n1, p1, q1 = (4,5,6)                   # m1=[]

def hampacking(a):
    return a, a**2, a**3
print(hampacking(2))                                                # In ra (2,4,8)
unpacking1, unpacking2, unpacking3 = hampacking(5)
print(unpacking2)                                                   # In ra 25

def fibonacci(n):
    a,b = 1,1
    for i in range(n):
        a, b = b, a+b                       # Cho phép hoán đổi 2 gtri
    return a

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
for i,j in enumerate(alphabet):                # Trả về 1 chuỗi dạng tuple, ptu đầu số nguyên, ptu sau gtri của nó
    print(i+1,'.', j, sep = '' )



# SET: tập dlieu ko có thứ tự(ko truy cập dc chỉ số), ko có trùng lặp

set1 = {(1,2,3), "dùng set(tuple,...) để khai báo cx dc", 123}           # ko dc chứa các ptu e kiểu dlieu tdoi dc như list, dictionary   
print(set1)                                                              # In ra có thể ko đúng thứ tự

set1.add((4,5,6))
set1.update({"Thêm phần tử"})
set1.update(("Câu nó sẽ bị tách ra thành từng chữ cái phân biệt, add thì ko bị"))     
print(set1)

set1.discard(4)                                                          # Xóa 1 ptu 
set1.pop()                                                               # Xóa 1 ptu bất kì
print(set1)

set2 = set1.copy()
set3 = frozenset(set1)                                                   # frozenset Là 1 tập bất biến, ko cho phép tdoi, tạo ra chỉ để ĐỌC
print(set2)

set4 = {1,2,3,(4,5,6),7,8,9}
set5 = {2,(4,5,6),8,10,12}
set6 = set4.union(set5)                                                  # Hợp
set7 = set4.intersection(set5)                                           # Giao
set8 = set4.difference(set5)                                             # Hiệu, thuộc set4, ko thuộc set5
set9 = set4.symmetric_difference(set5)                                   # Hiệu đối xúng
print(set8)
print(set9)

print(set4.issubset(set5))                                               # Ktra set4 có là con set5 ko
print(set4.issuperset(set5))                                             # Ktra set4 có là cha set5 ko
print(set4.isdisjoint(set5))                                             # Ktra set4 và set5 có tách rời nhau ko



# DICTIONARY: ko có thứ tự, mỗi gtr có thể thay đổi, lặp lại đc, tương ứng đúng 1 khóa, khóa là duy nhất
dict1 = dict({1:'A', 2:'B', 3:'C', 4:'D'})
print(dict1.get(5, "Gtri trả về khi ko có khóa đó"))                      # Trả về gtri ứng với khóa, nếu ko có khóa đó thì add gtri vào khóa đó
print(len(dict1))

dict2 = {
    "class 12T":{
        "HS Hoàng":{
            "Điểm thi tổ hợp":{
                "Toán": 9,
                "Vật lí": 10,
                "Tiếng anh": 8
            }
        }
    }
}
print("Điểm thi Vật lí là:",dict2.get("class 12T").get("HS Hoàng").get("Điểm thi tổ hợp").get("Vật lí"))       # In ra 10

print(dict2.items())                  # Trả về ds các cặp khóa và giá trị 
dict2.update({"class 12T":{"HS Hoàng":{"Điểm thi tổ hợp":{"Toán": 9, "Vật lí": 10,"Tiếng anh":9}}}})
print(dict2.items())

print(dict1.pop(2))                   # In ra B
print(dict1)

dict3 = [
        {'Name' : "Anh", 'Điểm': 10, 'TB': 1},
        {'Name' : "Bnh", 'Điểm':10, 'TB': 3},
        {'Name' : "Cnh", 'Điểm':2, 'TB': 2},
        {'Name' : "Dnh", 'Điểm': 10, 'TB':4}
]

sapxepdict = sorted(dict3, key = lambda i:(i['Điểm'],i['TB']), reverse= True) 
print(sapxepdict)  
sapxepdict = sorted(dict3, key = lambda i: i.get('Điểm'), reverse= True)                  # Sắp xếp điểm trước
print(sapxepdict)

# Kỹ thuật Comprehension:
output1 = [i if i>4 else 4 for i in range(1,10)]
print(output1)

x1 = int(input())
output2 = [x for x in range(x1) if "3" in str(x) ]
print(output2)



# LỚP VÀ ĐỐI TƯỢNG:
class SinhVien:                                 # Do ko khai báo hàm tạo, tự động cấp hàm tạo mặc định
    def thongtin(self):                         # Bắt buộc có self
        print(3*"Sinh viên\n")
taodoituong = SinhVien()
taodoituong.thongtin()

# Hàm tạo:
class hamtao1:
    def __init__(self, ID, name, birthday):         # ID,name,birthday là thuộc tính của đối tượng
        self.ID = ID
        self.name = name
        self.birthday = birthday
    def show(self):
        print("Mã sinh viên:{0}, Tên:{1}, Năm sinh:{2}".format(self.ID, self.name, self.birthday))
s1 = hamtao1(20,'Hoàng',2004)
s1.show()

class hamtao2:
    def __init__(self, name, salary, age=18):       # Tham số mặc định thì phải để cuối
        self.name = name
        self.age = age
        self.salary = salary
    def xem(self):
        print( self.name,self.age,"có lương là",self.salary )
gtrimacdinh_thamso_duocdung = hamtao2('Hoàng', 100)
gtrimacdinh_thamso_duocdung.xem()
gtrimacdinh_thamso_dcthaydoi = hamtao2('Hưng',90,16)
gtrimacdinh_thamso_dcthaydoi.xem()

# Trong 1 lớp ko tồn tại nhiều pthuc __init__
# Trong hàm tạo __init__ ko dc return lại giá trị

class Score:
  def __init__(self, point):            
    self.point = point
    print("Object with:",self.point,"has been create!")
    threshold=4.0
score_1 = Score(7.8)

# Thuộc tính của lớp và của đối tượng:
# Khi truy cập thuộc tính thông qua đối tượng của lớp, Python tìm e tính đó trong ds e tính của đối tượng.
# Nếu ko có, tiếp tục tìm kiếm trong danh sách thuộc tính của lớp.

class Tinhlaisuat:
    first_discount = 0.5
    def __init__(self, price):
        self.price = price
        self.discount = Tinhlaisuat.first_discount              # Định nghĩa gtri mặc định của mọi discount ban đầu là 0.5
    def thaydoi_laisuat (self, discount):
        self.discount = discount
    def in_giatri(self):
        return self.price * (1-self.discount)
laisuat1 = Tinhlaisuat(100)
print(laisuat1.in_giatri())                                     # In ra 50
laisuat2 = Tinhlaisuat(100)
laisuat2.thaydoi_laisuat(0.2)                                   # Thay đổi discount từ 0.5 thành 0.2
print(laisuat2.in_giatri())                                     # In ra 80

# Ví dụ khác:
class Circle:
  pi = 3.1416
  def __init__(self,radius):
    self.radius = radius
    self.pi = Circle.pi
  def circumference(self):
    return 2*self.pi*self.radius
  def areas(self):
    return self.pi*self.radius*self.radius
r=float(input())
circle = Circle(r)
print(f"PI: {Circle.pi}")
print(f"Radius: {r}")
print(f"Circumference: {circle.circumference()}")
print(f"Area: {circle.areas()}")

# BTAP: Quản lý Khóa học
class course:
    def __init__(self, name, year, id_number, lecturer, student_list):
        self.name = name
        self.year = year
        self.id_number = id_number
        self.lecturer = lecturer
        self.student_list = student_list
    def print_info (self):
        print(f"Họ và tên: {self.name}, sinh năm {self.year}, MSSV là {self.id_number}, giảng viên là {self.lecturer}")
        print(f"danh sách lớp gồm: {self.student_list}")

dsach1 = ["Anh","Bách","Chi","Đức","Hoàng"]
student1 = course("Hoàng",2004,20224855,"Mr.Nam",dsach1)
student1.print_info()
print(student1.id_number)                                       # In ra 20224855            

# Kế thừa:
class kethua(course):
    def __init__(self, cname, cyear, cid_number, clecturer, cstudent_list, account):
        super().__init__(cname, cyear, cid_number, clecturer, cstudent_list )
        self.account = account
    def in_giatri1(self):
        print(f"Họ và tên: {self.name}, sinh năm {self.year}, MSSV là {self.id_number}, giảng viên là {self.lecturer}, tkhoan là {self.account}")
student2 = kethua("Hoàng", 2004, 20224855, "Mr.Hieu", dsach1, 10001001)
student2.in_giatri1()

# Ví dụ khác:
class Rectangle:
  def __init__(self, length, width):
    self.length = length
    self.width = width
  def perimeter(self):
    return 2*(self.length + self.width)
  def area(self):
    return self.length * self.width
  def display(self):
    print(f"The length of rectangle is: {self.length}")
    print(f"The width of rectangle is: {self.width}")
    print("The perimeter of rectangle is:",self.perimeter())
    print("The area of rectangle is:", self.area())
class Parallelepipede(Rectangle):
  def __init__(self, length, width, height):
    super().__init__(length, width)
    self.height = height
  def volume(self):
    return self.length * self.width * self.height
length = float(input())
width = float(input())
myRectangle = Rectangle(length, width)
myRectangle.display()
height = float(input())
myParallelepipede = Parallelepipede(length, width, height)
print("The volume of myParallelepipede is:", myParallelepipede.volume())

# Tính đa hình:
pi = 3.14
class Shape:
    def __init__(self, name):
        self.name = name
    def area(self):
        pass                                # Bỏ qua ko có gì
    def ingiatri(self):
        print("Đây là hình cha")
class Hinhvuong(Shape):
    def __init__(self, length ):
        super().__init__(self)              # init("Hinhvuong") cũng được
        self.length = length
    def area(self):
        return self.length**2
    def ingiatri(self):                     # Giống lớp cha
        print("Đây là hình vuông")
class Hinhtron(Shape):
    def __init__(self, radius):
        super().__init__("Hinhtron")
        self.radius = radius
    def area(self):
        return pi*self.radius**2
Hinhvuong1 = Hinhvuong(4)
Hinhtron1 = Hinhtron(6)
Hinhvuong1.ingiatri()                  # In "Đây là hình vuông"
print(Hinhvuong1.area())
Hinhtron1.ingiatri()                   # In "Đây là hình cha", do Hinhtron ko có hàm ingiatri
                                       # Nên nó vẫn dùng hàm của lớp cha
print(Hinhtron1.area())


# NẠP CHỒNG TOÁN TỬ:
class vi_du:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __mul__(self, self1):          # Bắt buộc phải đúng tên hàm
        a = self.a * self1.a           # Hàm mul, sub,... chỉ có 2 biến, nhiều hơn bị lỗi
        b = self.b * self1.b 
        return a, b
t1 = vi_du(2, 3)
t2 = vi_du(5, 7)
print(t1 * t2)                         # In ra (10, 21)

# Ví dụ về xây dựng các phép toán vecto bằng nạp chồng:
class Vector:
  def __init__(self, point):
    self.point = point
  def __add__(self, other):
    if( len(self.point) != len(other.point) ):
      print("Size Error!")
    else:
      a=[]
      for i in range(len(self.point)):
        a.append( self.point[i] + other.point[i])
      return a
  def __sub__ (self, other):
    if( len(self.point) != len(other.point) ):
      print("Size Error!")
    else:
      a=[]
      for i in range(len(self.point)):
        a.append( self.point[i] - other.point[i])
      return a
  def __mul__ (self, other):
    if( len(self.point) != len(other.point) ):
      print("Size Error!")
    else:
      tichvohuong = 0
      for i in range(len(self.point)):
        tichvohuong += self.point[i] * other.point[i]
      return tichvohuong
  def __eq__ (self, other):
    if( len(self.point) != len(other.point) ):
      print("Size Error!")
    else:
      dem = 0
      for i in range(len(self.point)):
        if ( self.point[i] != other.point[i]):
          dem += 1
          break
      if dem == 0:
        return True
      if dem ==1:
        return False

vector1 = Vector([float(x) for x in input().split()])
vector2 = Vector([float(x) for x in input().split()])
print(vector1 + vector2)
print(vector1 - vector2)
print(vector1 * vector2)
print(vector1 == vector2)



