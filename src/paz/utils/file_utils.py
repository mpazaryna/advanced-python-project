from pathlib import Path
from typing import List, Tuple, Union

# Default PROJECT_ROOT
DEFAULT_PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent.parent


def get_project_root() -> Path:
    """
    Get the project root directory.

    Returns:
        Path: The path to the project root.
    """
    return DEFAULT_PROJECT_ROOT


def write_to_file(
    content: Union[str, List[Tuple[str, str]]],
    output_filename: str,
    persistent: bool = False,
    project_root: Path = None,
) -> Path:
    """
    Write content to a file in either the tmp or data directory.

    Args:
        content (Union[str, List[Tuple[str, str]]]): The content to write. If a string, writes directly.
                                                     If a list of tuples, each tuple should be (title, content).
        output_filename (str): The name of the file to save the content.
        persistent (bool): If True, save to data folder; if False, save to tmp folder.
        project_root (Path): Optional. The project root directory. If None, uses the default.

    Returns:
        Path: The path to the written file.
    """
    if project_root is None:
        project_root = get_project_root()

    output_dir = project_root / ("data" if persistent else "tmp")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file_path = output_dir / output_filename

    with open(output_file_path, "w", encoding="utf-8") as f:
        if isinstance(content, str):
            f.write(content)
        else:
            for title, text in content:
                f.write(f"Content from {title}: \n\n")
                f.write(text)
                f.write("\n\n" + "-" * 80 + "\n\n")

    return output_file_path
