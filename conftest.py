import pytest
from src.Exercise1 import Perimeter

@pytest.fixture()
def perimeter():
    return Perimeter()