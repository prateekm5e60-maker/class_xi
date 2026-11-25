sentence=input("enter your sentence::")
new_sentece=sentence.split()
largest=""
for i in new_sentece:
    if len(i)<len(largest):
        largest=i
print(f"the largeststring in the sentesce is{largest}")