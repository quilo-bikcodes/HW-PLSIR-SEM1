Even_Sum = 0
Odd_Sum = 0

Number = int(input("Please enter the Total Number of List Elements: "))

for i in range(Number+1):
    if i%2:
        Odd_Sum += i
    else:
        Even_Sum += i

print(f"Odd_Sum: {Odd_Sum}")
print(f"Even_Sum: {Even_Sum}")