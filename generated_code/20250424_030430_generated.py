def factorial(n):
  """Calculate the factorial of a non-negative integer."""
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)