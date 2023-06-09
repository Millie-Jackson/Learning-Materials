import tensorflow as tf

# Create Tensor
tensor_zero_d = tf.constant(4)
#print(tensor_zero_d)

tensor_one_d = tf.constant([2, 0, -3, 8, 90.])
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

# Descriptives
print(tensor_three_d.shape)