import json

json_dict = {"name" : "John", "age" : "30", "city" : "New York"}

with open("JSON_sample.json", mode="w") as f:
    json.dump(json_dict, f)