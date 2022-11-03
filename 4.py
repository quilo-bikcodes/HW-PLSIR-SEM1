num=int(input("Check for prime Nos.: "))
def main(x):
    for i in range(2,x//2+1):
        if x%i==0:
            return "Composite No."
    return "Prime No."

print(main(num))

# check prime nos