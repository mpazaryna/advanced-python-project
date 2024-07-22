# paz - Python Advanced Project

## Description

paz is an advanced Python project demonstrating best practices in Python development, including project structure, testing, documentation, and more.

## Workflow

```
poetry run black .
poetry run flake8
poetry run mypy src
poetry run pytest
poetry run docs
poetry run pre-commit run --all-files
```


## Installation

To install paz, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/paz.git
   cd paz
   ```

2. Install with Poetry:
   ```
   poetry install
   ```

## Usage

Here's a basic example of how to use paz:

```python
from paz import some_function

result = some_function()
print(result)
```

For more detailed usage instructions, please refer to the [full documentation](docs/build/html/index.html).

## Development

To set up the development environment:

1. Ensure you have Poetry installed.
2. Run `poetry install` to install all dependencies.
3. Run `poetry run pre-commit install` to set up the git hooks.

## Testing

Run the tests with:

```
poetry run pytest
```

## Building Documentation

To build the documentation:

```
poetry run docs
```

Then open `docs/build/html/index.html` in your web browser.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
