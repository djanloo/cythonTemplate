from multiprocessing import dummy
from os import chdir, path
from line_profiler import LineProfiler
from . import dummy_core

# Sets the working directory as the one with code
# Without this line line_profiler won't find the code
chdir(path.dirname(__file__))

arg = (2,1000)

# Same argument functions comparison
funcs = [dummy_core.primes, 
        dummy_core.primes_cy, 
        dummy_core.primes_cy_parallel, 
        dummy_core.primes_root,
        dummy_core.primes_cy_root,
        dummy_core.primes_cy_parallel_root,
        dummy_core.lprof_patch]

lp = LineProfiler()
lp.add_function(dummy_core.primes_cy)

for f in funcs:
    lp.add_function(f)
    wrap = lp(f)
    wrap(*arg)

lp.print_stats()