n=int(input("Enter the no. of apples you have:"))
mn=int(input("Enter the minimum no. of students:"))
mx=int(input("Enter the maximum no. of students:"))
if mn!=mx:
    for i in range(mn,mx+1):
        if n%i==0:
            print(f"{i} is divisor of {n}.")
        else:
            print(f"{i} is not divisor of {n}.")
else:
    print(f"It is not a range since maximum no. of students are equal to minimum no. of students i.e., {mn}={mx}.\nHence",end=' ')
    if n%mn==0:
        print(f"{mn} is divisor of {n}.")
    else:
        print(f"{mn} is not divisor of {n}.")