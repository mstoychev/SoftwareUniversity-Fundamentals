string = input().split()
searched_palindrome = input()
palindromes_lst = []
for word in string:
    if word == "".join(reversed(word)):  # join() method with the reversed() method because reversed() returns
        palindromes_lst.append(word)     # an iterator, not a string, so we should make it into one
print(palindromes_lst)
print(f"Found palindrome {palindromes_lst.count(searched_palindrome)} times")
