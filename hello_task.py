# Ray lets you run functions as remote tasks in the cluster. 
import ray

# Not requred in recent Ray versions
# ray.init()

# Define the square task.
@ray.remote
def square(x):
    return x * x

# Launch four parallel square tasks.
futures = [square.remote(i) for i in range(4)]

# Retrieve results.
print(ray.get(futures))
# -> [0, 1, 4, 9]