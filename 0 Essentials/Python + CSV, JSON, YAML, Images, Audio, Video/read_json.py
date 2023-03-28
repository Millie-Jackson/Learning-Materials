import json

with open("JSON_sample.json", mode="r") as f:
    json_dict = json.load(f)
    my_data = dict(json_dict)

print(my_data)