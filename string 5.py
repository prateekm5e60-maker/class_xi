text=input("enter your text ::")
p=text.split()
for i in p:
    print(i[0].upper()+ i[1:] , end="")

