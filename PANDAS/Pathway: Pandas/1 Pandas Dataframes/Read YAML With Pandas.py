import pandas as pd
from yaml import safe_load

file_name = "yaml_example.yaml"

def YAML_to_dataframe(path):

    with open(path, "r") as file:
        df = pd.json_normalize(safe_load(file))
    
    print(df.head(3))
    return 

YAML_to_dataframe(file_name)


