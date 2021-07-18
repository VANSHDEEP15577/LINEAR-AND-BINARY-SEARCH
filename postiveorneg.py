
w=int(input("ENTER THE NO.:"))
if w < 0:
    print(w,"IS A NEGATIVE NO.")
elif w == 0:
    print(w,"IS NEITHER POSITIVE NOR NEGATIVE")
else:
    print(w,"IS A POSITIVE NO.")
if w % 2 == 0:
    print(w,"IS A EVEN NO.")
else:
    print(w,"IS A ODD NO.")