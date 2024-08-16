# When you start a single-node Ray Cluster on your laptop, access the dashboard with the URL that
# Ray prints when it initializes (the default URL is http://localhost:8265) or with the context 
# object returned by ray.init.
import ray
import time

context = ray.init()
print(context.dashboard_url)
time.sleep(600)
