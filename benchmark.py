# import pyximport; pyximport.install()
from time import perf_counter
from rich import print

from dummy_pkg import setup
from dummy_pkg import dummy_core
from dummy_pkg.vanilla import PerfContext


N = 20_000
print(f"Primes searching benchmark (up to {N}):\n")
with PerfContext("global") as p:
    p.watch(dummy_core.primes, "python", args=(2,N) )
    p.watch(dummy_core.primes_cy, "cython", args=(2,N) )
    p.watch(dummy_core.primes_cy_parallel, "cython_parallel", args=(2,N) )
    p.watch(dummy_core.primes_root, "python_r", args=(2,N) )
    p.watch(dummy_core.primes_cy_root, "cython_r", args=(2,N) )
    p.watch(dummy_core.primes_cy_parallel_root, "cython_parallel_r", args=(2,N) )


