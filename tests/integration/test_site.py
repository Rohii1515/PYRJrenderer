import pytest
from PYRJrenderer import render_site
from PYRJrenderer.custom_exception import InvalidURLException


class TestRenderSite:
    URL_test_success_data = [
        ("http://pytorch.org", "success"),
        ("https://pytorch.org", "success"),
    ]

    URL_test_bad_data = [
        ("http://pytorch"),
        ("http//pytorch"),
        ("http:/pytorch"),
        ("http/pytorch"),
        ("http/pytorch"),
        ("pytorch.org"),
        ("http://asyef/"),
    ]
    
    """
        this method checks whether the test_success_data is valid else raise assertion failure
    """
    @pytest.mark.parametrize("URL, response", URL_test_success_data)
    def test_render_site_success(self, URL, response):
        assert render_site(URL) == response

    """
        this method checks the bad data and raies the InvalidURLException
    """
    @pytest.mark.parametrize("URL", URL_test_bad_data)
    def test_render_site_failed(self, URL):
        with pytest.raises(InvalidURLException):
            render_site(URL)