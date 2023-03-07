country_list = input().split(", ")
capital_list = input().split(", ")
country_dict = {country_list[index]: capital_list[index] for index in range(len(country_list))}

for key, value in country_dict.items():
    print(f"{key} -> {value}")