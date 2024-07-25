import pytest

from paz.utils.file_utils import write_to_file


@pytest.mark.parametrize("persistent", [True, False])
def test_write_to_file(tmp_path, persistent):
    content = [
        ("Test URL 1", "This is test content 1"),
        ("Test URL 2", "This is test content 2"),
    ]
    filename = "test_file.txt"

    file_path = write_to_file(content, filename, persistent, project_root=tmp_path)

    # Check if the file is in the correct directory
    expected_dir = "data" if persistent else "tmp"
    assert (
        file_path.parent.name == expected_dir
    ), f"File not in {expected_dir} directory"

    # Check if the file exists
    assert file_path.exists(), f"File not found at {file_path}"

    # Check the content of the file
    with open(file_path, "r", encoding="utf-8") as f:
        file_content = f.read()

    assert "This is test content 1" in file_content
    assert "This is test content 2" in file_content


# To run these tests, use: pytest tests/lab/test_async_scraper.py
