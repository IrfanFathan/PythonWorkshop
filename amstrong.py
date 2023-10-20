num=int(input("Enter a number"))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10
    print(temp)
if num==sum:
    print("Yup that was amstrong")
else:
    print("Yup that was not amstrong")    
    

    