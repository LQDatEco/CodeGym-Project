import math
#Nhập dữ liệu 3 cạnh
a = float(input("Nhập chiều dài cạnh a: "))
b = float(input("Nhập chiều dài cạnh b: "))
c = float(input("Nhập chiều dài cạnh c: "))
#Tính toán
s = (a+b+c)/2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print(" Chu vi của tam giác là: ", area)
