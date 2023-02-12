year_original = int(input())
year = year_original + 1
year_str = str(year)
while len(str(year_original)) != len(set(year_str)):
    year += 1
    year_str = str(year)

print(year)