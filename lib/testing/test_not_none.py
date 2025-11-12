#!/usr/bin/env python3

# testing/test_not_none.py
from not_none_functions import return_not_none

def test_return_not_none():
    """in not_none_functions, function 'return_not_none()' must not return None."""
    assert return_not_none() is not None, "return_not_none() returned None — it must return a non-None value"
