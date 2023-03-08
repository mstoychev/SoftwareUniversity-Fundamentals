legend = {"shards": 0, "fragments": 0, "motes": 0}

while True:
    if 250 <= legend["shards"] or 250 <= legend["fragments"] or 250 <= legend["motes"]:
        break
    line = input().lower().split()
    for i in range(0, len(line), 2):
        value = int(line[i])
        key = line[i + 1]
        if key not in legend.keys():
            legend[key] = value
        else:
            legend[key] += value
            if legend[key] >= 250:
                break

if legend["shards"] >= 250:
    legend["shards"] -= 250
    print("Shadowmourne obtained!")
elif legend["fragments"] >= 250:
    legend["fragments"] -= 250
    print("Valanyr obtained!")
elif legend["motes"] >= 250:
    legend["motes"] -= 250
    print("Dragonwrath obtained!")

print(f"shards: {legend['shards']}"
      f"\nfragments: {legend['fragments']}"
      f"\nmotes: {legend['motes']}")
del legend["shards"]
del legend["fragments"]
del legend["motes"]

for key, value in legend.items():
    print(f"{key}: {value}")
