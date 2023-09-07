import pytest
from PYRJrenderer import is_valid


"""
    URL_test_data is a test data list contains a list of URLS
"""
URL_test_data = [
    ("http://pytorch.org", True),
    ("https://pytorch.org", True),
    ("http://pytorch", False),
    ("http//pytorch", False),
    ("http:/pytorch", False),
    ("http/pytorch", False),
    ("http/pytorch", False),
    ("pytorch.org", False),
    ("http://asyef/", False),
]


"""
    this method test whether the given urls are valid or not by passing to the is_valid method
"""


@pytest.mark.parametrize("URL, response", URL_test_data)
def test_is_valid(URL, response):
    assert is_valid(URL) == response
