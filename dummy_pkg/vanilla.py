"""A module in vanilla python"""
from time import perf_counter
from rich import print
# Checks if cython stuff can be imported
from . import dummy_utils, dummy_core


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
        print(".", end="")

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

        print()
        for name in self.perfdict:
            print(f"[{colors[name]}]{name:<20}[/{colors[name]}] --> {self.perfdict[name]:8.3f} s (result: {self.resdict[name]})")

        print(f"\nContext {self.name} --> {self.exit_time - self.enter_time:.3f}")