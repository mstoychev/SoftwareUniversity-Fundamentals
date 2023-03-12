banned_words = input().split(", ")
text = input()
for curr_banned in banned_words:
    text = text.replace(curr_banned, "*" * (len(curr_banned)))

print(text)