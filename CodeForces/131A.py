word = input()
ans = word
if len(word) > 1 and word[1:].upper() == word[1:]:
    if word[0] == word[0].lower():
        ans = word.capitalize()
    else:
        ans = word.lower()
elif len(word) == 1 and word == word.lower():
    ans = word.upper()
elif len(word) == 1 and word == word.upper():
    ans = word.lower()
print(ans)
