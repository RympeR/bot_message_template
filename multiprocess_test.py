import os
from multiprocessing import Process, current_process

def square(x):
    x = x ** 2
    proc_id = os.getpid()
    print(f"Process id {proc_id}")
    process_name = current_process()
    
