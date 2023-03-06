n = int(input())
new_dict = {}
for _ in range(0, n):
    key = input()
    if key not in new_dict:
        new_dict[key] = []

    value = input()
    if value not in new_dict[key]:
        new_dict[key].append(value)

for word, synonyms in new_dict.items():
    print(f"{word} - {', '.join(synonyms)}")


