from functools import lru_cache

@lru_cache
def fibnachi(n):
    a, b = 0, 1
    for x in range(n):
        a, b = b, a + b
        if n == b:
          return True
    return False

print(fibnachi(int(input())))