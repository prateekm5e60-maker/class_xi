text=input("enter your text")
vowels="aeiou"
a_count=0
e_count=0
i_count=0
o_count=0
u_count=0
for i in text:
    if i in vowels and i=="a":
        a_cout+=1
    elif i in vowels and i=="e":
        e_count+=1
    elif  i in vowels and i=="i":
        i_count+=1
    elif i in vowels and i=="o":
        o_count+=1
    elif i in vowels and i=="u":
        u_count+=1
print(f"a is a {a_count}")
print(f"e is a {e_count}")
print(f"i is a {i_count}")
print(f"o is a {o_count}")
print(f"u is a {u_count}")