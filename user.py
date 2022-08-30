from unicodedata import name
import dummy_module
from time import perf_counter
from rich import print

class PerfContext:

    def __init__(self, name):
        self.name = name

    def watch(self, func, name="timer", args=None):
        watch_start = perf_counter()
        result = func(*args)
        watch_end = perf_counter()
        print(f"[green]{name}[/green] --> {watch_end - watch_start} (result: {result})")

    def __enter__(self):
        self.enter_time = perf_counter()
        return self
    
    def __exit__(self, *args):
        self.exit_time = perf_counter()
        print(f"Context {self.name} --> {self.exit_time - self.enter_time}")

N = 50_000

with PerfContext("global") as p:
    p.watch(dummy_module.primes, "python", args=(2,N) )
    p.watch(dummy_module.primes_cy, "cython", args=(2,N) )