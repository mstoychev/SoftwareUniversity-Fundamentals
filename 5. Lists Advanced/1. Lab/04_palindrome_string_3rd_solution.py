def palindrome_filtered(word):
    if word == word[::-1]:
        return word


words = input().split(" ")
searched_word = input()
palindrome_lst = [word for word in words if palindrome_filtered(word)]
print(palindrome_lst)
print(f"Found palindrome {palindrome_lst.count(searched_word)} times")


