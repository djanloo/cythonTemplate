"""Dummy module"""

from . import dummy_utils, vanilla

dummy_utils.urushibara_ruka(1)
vanilla.hey()

# Just python: uses def
def primes(range_from: int, range_til: int):
  """ Returns the number of found prime numbers using range"""
  prime_count = 0
  range_from = range_from if range_from >= 2 else 2
  for num in range(range_from, range_til + 1):
    for divnum in range(2, num):
      if ((num % divnum) == 0):
        break
    else:
      prime_count += 1
  return prime_count

# This will be compiled in c and wrapped in python: uses cpdef
cpdef primes_cy(int range_from, int range_til):
  """ Returns the number of found prime numbers using range"""
  cdef int prime_count = 0
  cdef int num
  cdef int divnum
  range_from = range_from if range_from >= 2 else 2
  for num in range(range_from, range_til + 1):
    for divnum in range(2, num):
      if ((num % divnum) == 0):
        break
    else:
      prime_count += 1
  return prime_count

# this is just c: it can't be seen from outside
cdef does_nothing():
  pass