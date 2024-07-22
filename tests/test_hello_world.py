"""This module contains tests for the hello_world function."""

import pytest

from paz.utils.hello_world import hello_world


def test_hello_world_default():
    """Test the hello_world function with default argument."""
    assert hello_world() == "Hello, World!"


def test_hello_world_custom_name():
    """Test the hello_world function with a custom name."""
    assert hello_world("Alice") == "Hello, Alice!"


@pytest.mark.parametrize(
    "name, expected",
    [
        ("", "Hello, !"),
        ("123", "Hello, 123!"),
        ("   ", "Hello,    !"),
    ],
)
def test_hello_world_edge_cases(name, expected):
    """Test the hello_world function with various edge cases."""
    assert hello_world(name) == expected
