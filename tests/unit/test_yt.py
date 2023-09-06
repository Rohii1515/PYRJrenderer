import pytest
from PYRJrenderer import get_time_info
from PYRJrenderer.custom_exception import InvalidURLException


good_URL_data = [
    ("https://youtu.be/gHCf5hUqYE4?si=E24wqu8iCL1dxDfx", 0),
    ("https://www.youtube.com/watch?v=gHCf5hUqYE4", 0),
    ("https://youtu.be/gHCf5hUqYE4?si=tfeubgrmVqerxDWY&t=30", 30),
    ("https://www.youtube.com/watch?v=gHCf5hUqYE4&t=30s", 30),
]

URL_id_bad_data = [
    (
        "https://youtu.be/gHCf5hUqYE454?si=E24wqu8iCL1dxDfx"
    ),  # exception becz added extra length to id
    (
        "https://www.youtube.com/watch?v=gHCf5hUqYE4&t"
    ),  # exception becz added extra &t to id
    (
        "https://youtu.be/gHCf5hUqYE4?si=tfeubgrmVqerxDWY&t==30"
    ),  # exception becz added extra = at the end
    (
        "https://www.youtube.com/watch?v==gHCf5hUqYE4&t=30s"
    ),  # exception becz added extra = at the start
]


@pytest.mark.parametrize("URL, response", good_URL_data)
def test_get_time_info(URL, response):
    assert get_time_info(URL) == response


@pytest.mark.parametrize("URL", URL_id_bad_data)
def test_get_time_info_failed(URL):
    with pytest.raises(InvalidURLException):
        get_time_info(URL)
