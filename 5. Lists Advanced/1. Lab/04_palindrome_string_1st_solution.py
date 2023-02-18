all_palindromes = []


def palindrome(lst):
    for word in lst:
        if word == word[::-1]:
            all_palindromes.append(word)
    return all_palindromes


text = input().split(" ")
searched_palindrome = input()
palindromes_list = palindrome(text)

print(palindromes_list)
print(f"Found palindrome {palindromes_list.count(searched_palindrome)} times")
