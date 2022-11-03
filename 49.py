num=int(input("Get GCD: "))
l=[]
def main(x):
    l.append(1)
    for i in range(2,x//2+1):
        if x%i==0:
            l.append(i)
    l.append(x)
         
    return f"So the factors are: {l}"
    

print(main(num))