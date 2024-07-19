# Project Workflow

1. **Install dependencies**:
   ```
   poetry install
   ```
   This installs all project dependencies specified in `pyproject.toml`.

2. **Run tests**:
   ```
   poetry run pytest
   ```
   This runs all your pytest tests.

3. **Format code with Black**:
   ```
   poetry run black .
   ```
   This formats all Python files in your project according to Black's style guide.

4. **Check for linting issues with Flake8**:
   ```
   poetry run flake8 .
   ```
   This checks your code for style and quality issues.

5. **Run type checking with MyPy**:
   ```
   poetry run mypy src tests
   ```
   This performs static type checking on your Python code.

6. **Run pre-commit hooks manually**:
   ```
   poetry run pre-commit run --all-files
   ```
   This runs all pre-commit hooks on all files, useful for checking your entire project.

7. **Install pre-commit hooks** (do this once after cloning the repository):
   ```
   poetry run pre-commit install -t pre-commit -t commit-msg
   ```
   This installs the pre-commit hooks so they run automatically before each commit.

8. **Update dependencies**:
   ```
   poetry update
   ```
   This updates your project dependencies to their latest versions within the constraints specified in `pyproject.toml`.

9. **Add a new dependency**:
   ```
   poetry add <package-name>
   ```
   This adds a new package to your project dependencies.

10. **Add a new development dependency**:
    ```
    poetry add --dev <package-name>
    ```
    This adds a new package to your development dependencies.

11. **Run your main script** (assuming `hello_world.py` is your main script):
    ```
    poetry run python src/paz/hello_world.py
    ```
    This runs your main Python script.

12. **Activate the virtual environment**:
    ```
    poetry shell
    ```
    This activates the project's virtual environment for the current terminal session.

13. **Check for security vulnerabilities** (if you've installed safety):
    ```
    poetry run safety check
    ```
    This checks your dependencies for known security vulnerabilities.

Remember, the pre-commit hooks (including Black, Flake8, and MyPy) will run automatically when you try to make a commit, catching issues before they make it into your repository. However, you can always run these tools manually as shown above to check your code at any time.

This workflow allows you to maintain code quality, ensure proper formatting, catch type errors, and keep your dependencies up to date throughout your development process.
