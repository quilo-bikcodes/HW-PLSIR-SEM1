x=int(input(" Enter No. of terms: "))
sum=0
for i in range(1,x+1):
    if i%2:
        sum+=i
print(f"The sum of od Nos. {sum}")