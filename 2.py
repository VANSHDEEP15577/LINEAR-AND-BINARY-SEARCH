list=[]
w=int(input("ENTER THE NO. OF ELEMENTS YOU WANT IN THE ARRAY:"))
mid=0
low=0
high=w-1
res=-1
for i in range(0,w):
    p=input("ENTER THE ELEMENT:")
    list.append(p)
y=input("ENTER THE ELEMENT TO BE SEARCHED:")
while low <= high:
    mid=(low+high) // 2
    if list[mid] < y:
        low = mid+1
    elif list[mid] > y:
        high = mid-1
    else:
        res=mid
res=-1
if res != -1:
    print("ELEMENT IS PRESENT AT INDEX",res)
else:
    print("ELEMENT IS NOT PRESENT IN ARRAY")
