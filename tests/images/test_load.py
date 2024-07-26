# import asyncio

import pytest
from PIL import Image

from paz.images.processors import load_image


@pytest.mark.asyncio
async def test_load_image():
    # Arrange
    test_image_name = (
        "test.png"  # Changed from "test.png.jpg" to match your earlier example
    )

    # Act
    result = await load_image(test_image_name)

    # Assert
    assert isinstance(result, Image.Image)
    assert result.format in ["PNG", "JPEG", "JPG"]  # Check if it's a valid image format
    assert (
        result.size[0] > 0 and result.size[1] > 0
    )  # Check if the image has valid dimensions
