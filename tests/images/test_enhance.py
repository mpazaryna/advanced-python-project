# File: test_enhance.py
import os

import pytest
from PIL import Image

from paz.images.enhance import enhance_document_image
from paz.images.load import load_image


@pytest.mark.asyncio
async def test_enhance_document_image_original():
    # Arrange
    test_image_name = "test.png"

    # Act
    original_image = await load_image(test_image_name)

    # Ensure the test image was loaded successfully
    assert isinstance(
        original_image, Image.Image
    ), f"Failed to load test image: {test_image_name}"

    # Process the image
    enhanced_image = await enhance_document_image(test_image_name)

    # Assert
    # Check if the result is a PIL Image
    assert isinstance(enhanced_image, Image.Image), "Result is not a PIL Image"

    # Check if the image is grayscale
    assert enhanced_image.mode == "L", "Resulting image is not grayscale"

    # Check if the image dimensions are the same as the original
    assert enhanced_image.size == original_image.size, "Image dimensions have changed"

    # Optionally, save the enhanced image for manual inspection
    enhanced_image_path = "test_enhanced.png"
    enhanced_image.save(enhanced_image_path)
    print(f"Enhanced image saved to {enhanced_image_path}")


@pytest.mark.asyncio
async def test_load_image():
    # Arrange
    test_image_name = "test.png"

    # Act
    loaded_image = await load_image(test_image_name)

    # Assert
    assert isinstance(
        loaded_image, Image.Image
    ), "load_image did not return a PIL Image"
    assert loaded_image.mode in [
        "RGB",
        "RGBA",
        "L",
    ], f"Unexpected image mode: {loaded_image.mode}"


@pytest.mark.asyncio
async def test_enhance_document_image_two():
    # Arrange
    test_image_name = "test.png"
    enhanced_image_path = os.path.join(os.getcwd(), "test_enhanced.png")

    # Act
    original_image = await load_image(test_image_name)

    # Ensure the test image was loaded successfully
    assert isinstance(
        original_image, Image.Image
    ), f"Failed to load test image: {test_image_name}"

    # Process the image
    enhanced_image = await enhance_document_image(test_image_name)

    # Assert
    # Check if the result is a PIL Image
    assert isinstance(enhanced_image, Image.Image), "Result is not a PIL Image"

    # Check if the image is grayscale
    assert enhanced_image.mode == "L", "Resulting image is not grayscale"

    # Check if the image dimensions are the same as the original
    assert enhanced_image.size == original_image.size, "Image dimensions have changed"

    # Save the enhanced image for manual inspection
    enhanced_image.save(enhanced_image_path)

    # Check if the enhanced image file was created
    assert os.path.exists(
        enhanced_image_path
    ), f"Enhanced image was not saved to {enhanced_image_path}"

    print(f"Enhanced image saved to {enhanced_image_path}")

    # Clean up: remove the saved enhanced image after the test
    os.remove(enhanced_image_path)
