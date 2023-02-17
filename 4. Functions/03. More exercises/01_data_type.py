def transform_input(typology, name):
    if typology == "int":
        result = int(name) * 2
        return print(result)
    elif typology == "real":
        result = float(name) * 1.5
        return print(f"{result:.2f}")
    elif typology == "string":
        return print(f"${name}$")

data_type = input()
text = input()
transform_input(data_type, text)

