import tensorflow as tf # For modeling
import pandas as pd     # For data processing
import seaborn as sns   # For visualization

data = pd.read_csv("train.csv")

sns.pairplot(data[["v.id", 
                   "on road old", 
                   "on road now", 
                   "years", 
                   "km", 
                   "rating", 
                   "condition", 
                   "economy", 
                   "top speed", 
                   "hp", 
                   "torque", 
                   "current price"]], diag_kind="kde")