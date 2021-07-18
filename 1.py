list=[]
w=int(input("ENTER THE NO. OF ELEMENTS YOU WANT:"))
for i in range(0,w):
    p=input("ENTER THE ELEMENT:")
    list.append(p)
y=input("ENTER THE ELEMENT TO BE SEARCHED:")
res=-1
for j in range(0,w):
    if list[j] == y:
        res=j
    else:
        res=-1
if res==-1:
    print("ELEMENT FOUND AT INDEX",res)
else:
    print("ELEMENT NOT FOUND")