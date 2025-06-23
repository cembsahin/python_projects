# log_monitor.py

def read_log_file(filepath):
    with open(filepath, "r") as f:
        for line in f:
            yield line.strip()  # remove newline characters
#fjasdkljfaskd

