list=[]
w=int(input("ENTER THE NO. OF ELEMENTS TO BE WRITTEN:"))
for i in range(0,w):
    p=int(input("ENTER THE ELEMENT:"))
    list.append(p)
list.sort()
print("THE LIST IN ACCENDING ORDER WILL BE",list)