# import pyximport; pyximport.install()
# from dummy_pkg import setup
from dummy_pkg import dummy_core, vanilla
from time import perf_counter
from rich import print

vanilla.hey()

class PerfContext:
    """Dummy performance context"""

    def __init__(self, name):
        self.name = name
        self.perfdict = {}
        self.resdict = {}

    def watch(self, func, name="timer", args=None):

        watch_start = perf_counter()
        result = func(*args)
        watch_end = perf_counter()
        self.perfdict[name] = watch_end - watch_start
        self.resdict[name] = result

    def __enter__(self):
        self.enter_time = perf_counter()
        return self
    
    def __exit__(self, *args):
        self.exit_time = perf_counter()

        colors = {}
        for name in self.perfdict:
            colors[name] = "blue"

        colors[min(self.perfdict, key=self.perfdict.get)] = "green"
        colors[max(self.perfdict, key=self.perfdict.get)] = "red"


        for name in self.perfdict:
            print(f"[{colors[name]}]{name:<15}[/{colors[name]}] --> {self.perfdict[name]:8.3f} s (result: {self.resdict[name]})")

        print(f"\nContext {self.name} --> {self.exit_time - self.enter_time:.3f}")

N = 25_000
print(f"Primes searching benchmark (up to {N}):\n")
with PerfContext("global") as p:
    p.watch(dummy_core.primes, "python", args=(2,N) )
    p.watch(dummy_core.primes_cy, "cython", args=(2,N) )
    p.watch(dummy_core.primes_cy_parallel, "cython_parallel", args=(2,N) )


