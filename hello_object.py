# Ray stores task and actor call results in its distributed object store, 
# returning object references that can be later retrieved.
import ray
import numpy as np

# Define a task that sums the values in a matrix.
@ray.remote
def sum_matrix(matrix):
    return np.sum(matrix)

# Call the task with a literal argument value.
print(ray.get(sum_matrix.remote(np.ones((100, 100)))))
# -> 10000.0

# Put a large array into the object store.
matrix_ref = ray.put(np.ones((1000, 1000)))

# Call the task with the object reference as an argument.
print(ray.get(sum_matrix.remote(matrix_ref)))
# -> 1000000.0