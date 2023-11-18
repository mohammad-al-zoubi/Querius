import time


def generate_timestamp():
    current_timestamp = time.time()
    current_timestamp_long = int(current_timestamp)
    return current_timestamp_long
