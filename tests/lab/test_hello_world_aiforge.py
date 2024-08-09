"""This module contains tests for the hello_world function."""

from aiforge.lab.hello_world import greet


def test_greet_default():
    """Test the hello_world function with default argument."""
    assert greet() == "Hello, World!"


def test_greet_custom():
    """Test the hello_world function with default argument."""
    assert greet("Alice") == "Hello, Alice!"
