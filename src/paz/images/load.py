# Content of _load.py:
import logging
from io import BytesIO

from PIL import Image

from paz.utils.file_utils import get_file

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def load_image(file_name: str) -> Image.Image:
    """
    Asynchronously load an image file using the get_file utility.

    Args:
        file_name (str): The name of the image file in the tmp folder.

    Returns:
        Image.Image: A Pillow Image object.

    Raises:
        FileNotFoundError: If the file doesn't exist in the specified location.
        IOError: If the file cannot be read or is not a valid image.
    """
    try:
        # Get the file content as bytes
        image_data = get_file(file_name, persistent=False, binary=True)

        # Create an image object from the bytes data
        image = Image.open(BytesIO(image_data))

        return image
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Image file not found: {file_name}") from e
    except IOError as e:
        raise IOError(f"Error loading image {file_name}: {str(e)}") from e
