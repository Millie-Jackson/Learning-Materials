import csv
import json
import yaml

# CSV
# Open
with open('Salaries.csv', mode='r', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for n, row in enumerate(reader):
        print(','.join(row))
        if n == 5: # Read only the first five entries
            break

# Save
my_list = [['Sparky', 7, 'Brown', 'Corgi'], ['Fido', 4, 'White', 'Husky']]

with open('Dogs.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'Age', 'Colour', 'Breed'])
    writer.writerows(my_list)

# JSON
with open('JSON_sample.json', mode='r') as f:
    json_dict = json.load(f)

print("JSON type: ", type(json_dict)) # Its a dictionary
print("JSON: ", json_dict)

# Save
test_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
with open('JSON_test.json', mode='w') as f:
    json.dump(test_dict, f)

# Will not work with single quotes!
x =  '{"name": "John", "age": 30, "city": "New York"}'
y = json.loads(x)
print("JSON: ", y)
print("JSON type: ", type(y))

# JSON String
test_dict = {'a': 3, 'b': 4}
new_json = json.dumps(test_dict)
print("String JSON", new_json)

# YAML
# Open
with open('yaml_example.yaml', 'r') as stream:
    data_loaded = yaml.safe_load(stream)

print("YAML type: ", type(data_loaded))
print("YAML: ", data_loaded)
print("YAML keys: ", data_loaded.keys())

# Save
with open('JSON_sample.json', mode='r') as f:
    my_dict = json.load(f)

print(my_dict)

with open('YAML_from_JSON.yaml', 'w') as f:
        yaml.dump(my_dict, f)