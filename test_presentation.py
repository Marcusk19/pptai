import unittest
from unittest.mock import patch, MagicMock
from main import create_ppt


class TestPresentationCreation(unittest.TestCase):
    def setUp(self):
        # Sample valid YAML content for testing
        self.valid_yaml = """
- slide1:
    title: "Introduction"
    points:
      - "First point"
      - "Second point"
    image_prompt: "A test image"
- slide2:
    title: "Content"
    points:
      - "Another point"
    image_prompt: "Another test image"
"""
        # Invalid YAML content
        self.invalid_yaml = """
- slide1:
    title: "Bad YAML
    points:
      - unclosed quote"
"""
        # Empty YAML content
        self.empty_yaml = ""

        # YAML with missing required fields
        self.missing_fields_yaml = """
- slide1:
    points:
      - "Just points"
"""

    @patch("pptx.Presentation")
    @patch("main.generate_image")
    @patch("main.download_image")
    def test_valid_yaml_content(self, mock_download, mock_generate, mock_presentation):
        # Setup mocks
        mock_prs = MagicMock()
        mock_slide = MagicMock()
        mock_shapes = MagicMock()
        mock_title = MagicMock()
        mock_placeholder = MagicMock()

        mock_presentation.return_value = mock_prs
        mock_prs.slides.add_slide.return_value = mock_slide
        mock_slide.shapes = mock_shapes
        mock_shapes.title = mock_title
        mock_shapes.placeholders = {1: mock_placeholder}

        # Mock image generation
        mock_generate.return_value = "http://fake-url.com/image.png"
        mock_download.return_value = MagicMock()

        # Test the function
        create_ppt(self.valid_yaml)

        # Assertions
        self.assertTrue(mock_prs.slides.add_slide.called)
        self.assertTrue(mock_prs.save.called)
        mock_prs.save.assert_called_once_with("generated_presentation.pptx")

    @patch("pptx.Presentation")
    def test_invalid_yaml(self, mock_presentation):
        # Test with invalid YAML
        create_ppt(self.invalid_yaml)
        mock_presentation.return_value.save.assert_not_called()

    @patch("pptx.Presentation")
    def test_empty_yaml(self, mock_presentation):
        # Test with empty YAML
        create_ppt(self.empty_yaml)
        mock_presentation.return_value.save.assert_not_called()

    @patch("pptx.Presentation")
    @patch("main.generate_image")
    @patch("main.download_image")
    def test_missing_fields(self, mock_download, mock_generate, mock_presentation):
        # Setup mocks
        mock_prs = MagicMock()
        mock_slide = MagicMock()
        mock_shapes = MagicMock()
        mock_title = MagicMock()
        mock_placeholder = MagicMock()

        mock_presentation.return_value = mock_prs
        mock_prs.slides.add_slide.return_value = mock_slide
        mock_slide.shapes = mock_shapes
        mock_shapes.title = mock_title
        mock_shapes.placeholders = {1: mock_placeholder}

        # Test the function
        create_ppt(self.missing_fields_yaml)

        # Verify it handles missing fields gracefully
        self.assertTrue(mock_prs.slides.add_slide.called)
        self.assertTrue(mock_prs.save.called)

    @patch("pptx.Presentation")
    @patch("main.generate_image")
    @patch("main.download_image")
    def test_image_generation_failure(
        self, mock_download, mock_generate, mock_presentation
    ):
        # Setup mocks
        mock_prs = MagicMock()
        mock_slide = MagicMock()
        mock_shapes = MagicMock()
        mock_title = MagicMock()
        mock_placeholder = MagicMock()

        mock_presentation.return_value = mock_prs
        mock_prs.slides.add_slide.return_value = mock_slide
        mock_slide.shapes = mock_shapes
        mock_shapes.title = mock_title
        mock_shapes.placeholders = {1: mock_placeholder}

        # Mock image generation failure
        mock_generate.side_effect = Exception("Image generation failed")

        # Test the function
        create_ppt(self.valid_yaml)

        # Verify presentation is still created despite image failure
        self.assertTrue(mock_prs.slides.add_slide.called)
        self.assertTrue(mock_prs.save.called)


if __name__ == "__main__":
    unittest.main()
