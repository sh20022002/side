import timeit
import functools
import psutil

def time_and_resource_usage(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = timeit.default_timer()
        start_cpu = psutil.cpu_percent()
        start_mem = psutil.virtual_memory().percent

        result = func(*args, **kwargs)

        end_time = timeit.default_timer()
        end_cpu = psutil.cpu_percent()
        end_mem = psutil.virtual_memory().percent

        print(f"Function: {func.__name__}")
        print(f"Execution time: {end_time - start_time:.4f} seconds")
        print(f"CPU usage: {end_cpu - start_cpu:.2f}%")
        print(f"Memory usage: {end_mem - start_mem:.2f}%")

        return result
    return wrapper