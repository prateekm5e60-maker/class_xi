s=input("enter your string ::")
longest=""
for start in range (len(s)):
    for end in range(start,len(s)):
        substring=s[start:end+1]
        if substring==substring[::-1]:
            if len(substring)>len(longest):
                longest=substring

print("longest palindromic substrind:",longest)