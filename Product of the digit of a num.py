num=int(input("Enter a num:"))
b=1
while num!=0:
    a=num%10#This condition will give the remainder value that store in the a variable
    b*=a#This condition will multi the remainder value * 1 and store num in b variable
    num=num//10#This condition will give the quiotent value and repeated the all condition
print(f"Product of the num:{b}")