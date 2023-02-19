# Using comprehension; only those words whose length is even
text = input().split()
result = [word for word in text if len(word) % 2 == 0]
for element in result:
    print(element)
