s=input("enter your string  ::")
best=""
for start in range(len(s)):
    current=""
    for end in range(start,len(s)):
        if s[end] in current:
            break

        current+=s[end]
        if len(current)>len(best):
            best=current


print("longest substring without repeating charaters",best)