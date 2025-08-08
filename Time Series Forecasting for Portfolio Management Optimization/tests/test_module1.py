import pytest
from src.modules.module1 import some_function

def test_some_function():
    assert some_function() == "Hello from module1"
