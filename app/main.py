try:
    import os
    import sys
    # Add working dir to PYTHONPATH...
    sys.path.append(os.getcwd())
    from spark.stream import SparkStream
except ImportError as e:
    raise ImportError(e)

print("Running...")
spark = SparkStream()