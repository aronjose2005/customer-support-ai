import pytest
from src.customer_support import generate_support_response

def test_generate_support_response():
    response = generate_support_response("How do I return a product?", language="en")
    assert isinstance(response, str)
    assert len(response) > 0
