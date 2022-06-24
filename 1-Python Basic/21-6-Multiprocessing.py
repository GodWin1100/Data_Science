import multiprocessing
import datetime as dt
import time
import random
import os


def time_interval(sec: int):
    """Print time at random given interval

    Args:
        sec (int): seconds
    """
    time.sleep(sec)
    print(f"PID: {os.getpid()}, Waited {sec}, Time: {dt.datetime.now()}")


if __name__ == "__main__":
    for n in range(3):
        process = multiprocessing.Process(target=time_interval, args=(random.randint(1, 5),))
        process.start()
        process.join()
