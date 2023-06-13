import tensorflow as tf
import numpy as np

# Create Tensor
tensor_zero_d = tf.constant(4)
#print(tensor_zero_d)

tensor_one_d = tf.constant([2, 0, -3, 8, 90.], dtype=tf.float64)
#print(tensor_one_d)

tensor_two_d = tf.constant([
    [1, 2, 0],
    [3, 5, -1],
    [1, 5, 6],
    [2, 3, 8]
    ])
#print(tensor_two_d)

tensor_three_d = tf.constant([
    [[1, 2, 0],
     [3, 5, -1]],

    [[10, 2, 0],
     [1, 0, 2]],
 
    [[5, 8, 0],
     [2, 7, 0]],

    [[2, 1, 9],
     [4, -3, 32]]
    ])
#print(tensor_three_d)

tensor_four_d = tf.constant([
    [
        [[1, 2, 0],
        [3, 5, -1]],

        [[10, 2, 0],
        [1, 0, 2]],
 
        [[5, 8, 0],
        [2, 7, 0]],

        [[2, 1, 9],
        [4, -3, 32]]
    ],

    [
        [[13, 26, 0],
        [3, 5, -12]],

        [[10, 2, 0],
        [1, 0, 23]],
 
        [[5, 8, 0],
        [2, 73, 0]],

        [[2, 1, 9],
        [4, -30, 32]]
    ],

    [
        [[103, 26, 0],
        [3, 50, -12]],

        [[100, 2, 0],
        [1, 0, 23]],
 
        [[5, 28, 0],
        [2, 3, 0]],

        [[22, 1, 9],
        [44, -320, 32]]
     ]
    ])
#print(tensor_four_d)

# Casting
tensor_one_d = tf.constant([2, 0, -3, 8, 90.], dtype=tf.float64)
casted_tensor_one_d = tf.cast(tensor_one_d, dtype=tf.int16)
casted_bool_tensor_one_d = tf.cast(tensor_one_d, dtype=tf.bool)
#print(tensor_one_d)
#print(casted_tensor_one_d)
#print(casted_bool_tensor_one_d)

tensor_bool = tf.constant([True, True, False])
#print(tensor_bool)

tensor_string = tf.constant("Hello World")
tensor_string_list = tf.constant(["Hello World", "Hi"])
#print(tensor_string)
#print(tensor_string_list)

np_array = np.array([1, 2, 4])
converted_tensor = tf.convert_to_tensor(np_array)
#print(np_array)
#print(converted_tensor)

eye_tensor = tf.eye(
    num_rows=5,
    num_columns=3,
    batch_shape=[2,4], # 2 by 4 matrix
    dtype = tf.dtypes.float32,
    name=None
)
print(eye_tensor)

# Descriptives
#print(tensor_three_d.shape)