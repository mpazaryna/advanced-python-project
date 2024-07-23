"""This module provides a simple greeting function."""


def hello_world(name: str = "World") -> str:
    """
    Return a greeting message.

    Args:
        name (str, optional): The name to greet. Defaults to "World".

    Returns:
        str: A greeting message.
    """
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(hello_world())
