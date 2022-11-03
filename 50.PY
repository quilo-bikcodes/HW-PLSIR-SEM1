a = int(input("Enter side 1 length: "))
b = int(input("Enter side 2 length: "))
c = int(input("Enter side 3 length: "))

if a==b and b==c and c==a:
    print("Equilateral Triangle")
elif a==b or b==c or c==a:
    print("Isoceles Triangle")
else:
    print("Scalene Triangle")