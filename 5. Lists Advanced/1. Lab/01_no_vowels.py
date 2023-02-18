word = input()
vowels = ['a', 'o', 'u', 'e', 'i']  #have to use .lower() method
removed_vowels = [filtered for filtered in word if not filtered.lower() in vowels]
print("".join(removed_vowels))