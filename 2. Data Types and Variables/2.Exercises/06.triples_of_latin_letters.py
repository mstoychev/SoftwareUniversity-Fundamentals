#Write a program to read an integer N and print all triples of the first N
# small Latin letters, ordered alphabetically.
start = 97         # ascii "a"
n = int(input())
for first in range(start, start + n):
    for second in range(start, start +n):
        for third in range(start, start + n):
            print(chr(first), chr(second), chr(third), sep="")

