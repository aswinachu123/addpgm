i=int(input("enter a number"))
s=0
while(i>0):
    r=int(i%10)
    s=s*10+r
    i=int(i/10)
print(s)    