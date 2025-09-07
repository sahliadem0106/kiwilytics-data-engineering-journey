number=["one","twoo","three"]
for x in number:
    print(x)
number2=[1,2,3,4,5]
for x in number2:
    print(x+50)
#---------------------
for x in "adem":     
    print(ord(x))
for i in range(4):
    print(i)
print("loop2")
for i in range(1,5):
    print(i)
print("loop3")
for i in range(1,10,2):
    print(i)
#nested for loop
print("nested for loop") 
x0=[1,2]
x1=[1,2,3,4,5]
for i in x0:
    for j in x1:
        print(i*j)