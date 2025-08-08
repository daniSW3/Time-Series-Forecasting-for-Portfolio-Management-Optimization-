import pytest
from src.modules.module2 import another_function

def test_another_function():
    assert another_function() == "Hello from module2"
