##a=int(input())
##for i in range(a):
##    for j in range(a-i):
##        print(str(j+1)+"|",end="")
##    print("")


##a=int(input())
##for i in range(a):
##    for j in range(a-i):
##        print("  ",end="")
##
##    for j in range(i+1):
##        print(str(j+1)+"|",end="")
##    print("")
##
##a=int(input())
##for i in range(a):
##    for j in range(i):
##        print("  ",end="")
##
##    for j in range(a-i):
##        print(str(j+1)+"|",end="")
##    print("")


##my_sum = 0
##for i in range (10):
##    x = int(input())
##    my_sum=my_sum+x
##avg = my_sum/10
##print(avg)

##a=input()
##for i in range(len(a)):
##               
##    print(a[i]+" ",end="")

x=int(input())
y= True
for i in range(2,x-1):
    if(x%i==0):
        print("ไม่ใช่จำนวนเฉพาะ")
        y = False
        break
if y :
    print("จำนวนเฉพาะ")
    print
    
