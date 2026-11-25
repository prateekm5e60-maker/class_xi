text1=input("enter your text:")
text2=input("enter your text:")
if sorted(text1)==sorted(text2):
    print(f"{text1} and {text2} are an angram")
else:
    print(f"{text1} and {text2} are not an angram")