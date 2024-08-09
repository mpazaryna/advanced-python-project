# Financial Risk Assessment Pipeline

![Python CI](https://github.com/mpazaryna/advanced-python-project/actions/workflows/.ci.yml/badge.svg?branch=main)

## Description

This is an advanced Python project demonstrating best practices in Python development.

## Usage

For more detailed usage instructions, please refer to the [full documentation](docs/build/html/index.html).

## Development Setup

To set up the development environment:

1. Ensure you have Poetry installed.
1. Run `poetry install` to install all dependencies.
1. Run `poetry run pre-commit install` to set up the git hooks.

## Testing

Run the tests with:

```bash
poetry run pytest
```

## Building Documentation

To build the documentation:

```bash
poetry run docs
```

Then open `docs/build/html/index.html` in your web browser.

## Workflow

```bash
poetry run black .
poetry run flake8
poetry run mypy src
poetry run pytest
poetry run docs
poetry run pre-commit run --all-files
```

## AI Forge

```bash
poetry update aiforge
```

## Contributing

No contributions are being accepted at this time.

## Project References

- [Curriculum](./docs/curriculum.md)
- [Project Plan](./docs/project_plan.md)
- [White Paper](./docs/white_paper.md)
- [Project Documentation](./docs/build/html/index.html)
- [Workflow](./docs/workflow.md)
- [Financial Risk Assessment: Perplexity.ai](https://www.perplexity.ai/search/what-is-financial-risk-assessm-D7YD5H32TIOXZthVY9zNjQ)
- [AI Forge](https://github.com/mpazaryna/aiforge)

## Techical References

- [Poetry](https://python-poetry.org/)
- [Black](https://black.readthedocs.io/en/stable/)
- [Flake8](https://flake8.pycqa.org/en/latest/)
- [Mypy](https://mypy.readthedocs.io/en/stable/)
- [Pytest](https://docs.pytest.org/en/stable/)
- [Sphinx](https://www.sphinx-doc.org/en/master/)
- [Pre-commit](https://pre-commit.com/)
