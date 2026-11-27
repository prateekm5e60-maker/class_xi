sentence=input("enter your sentence::")
output="" 
for i in sentence:
    n=sentence.count(i)
    if i not in output:
      output=output+i+str(n)
print(output)