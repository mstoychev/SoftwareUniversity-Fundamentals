country_list = input().split(", ")
capital_list = input().split(", ")
country_dict = {key: value for key, value in zip(country_list, capital_list)}
# country_dict = dict(zip(country_list, capital_list))
for key, value in country_dict.items():
    print(f"{key} -> {value}")



