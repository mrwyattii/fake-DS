import pytest
from fake_ds import init_inference

def test_inference():
    assert init_inference("gpt")
