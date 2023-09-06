import pytest
from PYRJrenderer import render_YouTube_video
from PYRJrenderer.custom_exception import InvalidURLException

class TestYTvideoRenderer:
    URL_test_success_data = [
        ("https://youtu.be/gHCf5hUqYE4?si=E24wqu8iCL1dxDfx", "success"),
        ("https://www.youtube.com/watch?v=gHCf5hUqYE4", "success"),
        ("https://www.youtube.com/watch?v=gHCf5hUqYE4&t=30s", "success"),
    ]
    URL_test_bad_data = [
        ("https://www.youtube.com/watch?v=gHCf5hUqYE4ahesbf"),
        ("https://www.youtube.com/watch?v=gHCf5hUqYE4&t00"),
        ("https://www.youtube.com/watch?v=gHCf5hUqYE4&t__"),
        ("https://youtu.be/gHCf5hUqYE454?si=E24wqu8iCL1dxDfx"),
        ("https://www.youtube.com/watch?v=gHCf5hUqYE4&t"),
        ("https://youtu.be/gHCf5hUqYE4?si=tfeubgrmVqerxDWY&t==30"),
        ("https://www.youtube.com/watch?v==gHCf5hUqYE4&t=30s"),
    ]
    
    @pytest.mark.parametrize("URL, response", URL_test_success_data)
    def test_render_YT_success(self, URL, response):
        assert render_YouTube_video(URL) == response
        
    @pytest.mark.parametrize("URL", URL_test_bad_data)
    def test_render_YT_failed(self, URL):
        with pytest.raises(InvalidURLException):
            render_YouTube_video(URL)