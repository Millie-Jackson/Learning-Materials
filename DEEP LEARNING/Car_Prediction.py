import tensorflow as tf # For modeling
import pandas as pd     # For data processing
import seaborn as sns   # For visualization
from tensorflow.keras.layers import Normalization, Dense

#  Load data set
data = pd.read_csv("train.csv")

# Visualise initial data set
sns.pairplot(data[["years", 
                   "km", 
                   "rating", 
                   "condition", 
                   "economy", 
                   "top speed", 
                   "hp", 
                   "torque", 
                   "current price"]], diag_kind="kde")

## DATA PREPERATION  ##

# CREATE TENSOR
tensor_data = tf.constant(data)
#print(tensor_data.shape)

# TEST TENSOR
tensor_data = tf.cast(tensor_data, tf.float32)
#print(tensor_data)

# SHUFFLE DATA SET
tensor_data = tf.random.shuffle(tensor_data)

# SET THE IMPUT VALUES
x = tensor_data[:, 3:-1] # Skip the columns we dont want
#print(x.shape)

# SET THE OUTPUT VALUES
y = tensor_data[:, :-1] # Skip the columns we dont want
y = tf.expand_dims(y, axis=-1) # Expand dimensions
#print(y.shape)

# NORMALISE THE INPUT
normalizer = Normalization()
normalizer.adapt(x)
normalizer(x)

# CREATE THE MODEL
model = tf.keras.Sequential([normalizer, # Stack up the layers of the model
                             Dense(1)])
model.summary()