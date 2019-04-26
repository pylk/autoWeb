import time
from AutoFramework.utils.logger import logger
import random

def timeit(func):
    def wrapper(a, b):
        init_time = time.time()
        value = func(a, b)
        logger.info("module: "+func.__module__+"function: "+func.__name__+"Time Elapsed: %s "%(time.time() - init_time))
        return value
    return wrapper

@timeit
def sleepadd(a,b):
    # time.sleep(random.random())
    time.sleep(3)
    return a+b

if __name__=="__main__":
    sleepadd(4,5)