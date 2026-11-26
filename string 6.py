text=input("enter your text ::")
p=text.split()
for i in p:
    print(i[::-1]   , end= " ")