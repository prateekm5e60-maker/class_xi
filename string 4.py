word=input("enter your strimg")
new_str=""
for i in word:
    if i  not in new_str:
        new_str=new_str+i
print(new_str)
