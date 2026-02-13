# Contributing to Ark Settings Generator

First off, thank you for considering contributing to Ark Settings Generator! It's people like you that make it such a great tool.

## Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the issue list as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible:

* **Use a clear and descriptive title**
* **Describe the exact steps which reproduce the problem**
* **Provide specific examples to demonstrate the steps**
* **Describe the behavior you observed after following the steps**
* **Explain which behavior you expected to see instead and why**
* **Include screenshots and animated GIFs if possible**

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, please include:

* **Use a clear and descriptive title**
* **Provide a step-by-step description of the suggested enhancement**
* **Provide specific examples to demonstrate the steps**
* **Describe the current behavior and expected behavior**
* **Explain why this enhancement would be useful**

### Pull Requests

* Fill in the required template
* Follow the Python code style
* Include appropriate test cases
* Update documentation as needed
* End all files with a newline

## Development Setup

### Prerequisites

- Python 3.8 or higher
- Git
- Virtual environment support (recommended)

### Getting Started

1. **Fork the repository** on GitHub

2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/your-username/Ark-Settings-Generator.git
   cd "Ark Settings Generator"
   ```

3. **Create a virtual environment**:
   ```bash
   python -m venv .venv
   .venv\Scripts\Activate.ps1  # Windows PowerShell
   source .venv/bin/activate    # Linux/Mac
   ```

4. **Install development dependencies**:
   ```bash
   cd source
   pip install -r requirements.txt
   pip install pillow pytest
   ```

5. **Create a new branch** for your changes:
   ```bash
   git checkout -b feature/your-feature-name
   ```

6. **Make your changes**

7. **Run tests**:
   ```bash
   pytest tests/ -v
   ```

8. **Build and test the executable**:
   ```bash
   python -m PyInstaller --clean --noconfirm ArkSettingsGenerator.spec
   # Test the executable in source/dist/ArkSettingsGenerator.exe
   ```

9. **Commit your changes**:
   ```bash
   git commit -m "Add your commit message here"
   ```

10. **Push to your fork**:
    ```bash
    git push origin feature/your-feature-name
    ```

11. **Create a Pull Request** on GitHub

## Code Style

### Python

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guidelines
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep lines reasonably short (max 100 characters)

### Example

```python
def calculate_taming_time(base_time: float, multiplier: float) -> float:
    """
    Calculate taming time based on multiplier.
    
    Args:
        base_time: Base taming time in hours
        multiplier: Taming speed multiplier (higher = faster)
    
    Returns:
        Calculated taming time in hours
    """
    if multiplier <= 0:
        raise ValueError("Multiplier must be positive")
    return base_time / multiplier
```

## Testing

- Write tests for new features
- Ensure all tests pass before submitting a PR
- Test both GUI functionality and core logic
- Include edge cases in tests

### Running Tests

```bash
pytest tests/ -v
```

### Test Coverage

We aim for at least 80% code coverage on core logic. Check coverage with:

```bash
pytest tests/ --cov=source --cov-report=html
```

## Documentation

- Update README.md if adding features
- Add docstrings to all functions
- Update CHANGELOG.md with your changes
- Comment complex logic

## Commit Messages

- Use clear, descriptive commit messages
- Start with a verb: "Add", "Fix", "Update", "Remove", etc.
- Keep commits focused on single features/fixes

Examples:
- ✅ `Add mod reordering functionality`
- ✅ `Fix window dragging performance issue`
- ✅ `Update README with new features`
- ❌ `fixed stuff`
- ❌ `changes`

## Pull Request Process

1. Update the README.md with any new features or changes
2. Update CHANGELOG.md with notes on your changes
3. Increase version numbers in version.py
4. Run tests and ensure they pass
5. Ensure code follows our style guidelines
6. Create the Pull Request with a clear description

## Recognition

Contributors who make significant improvements will be recognized in:
- README.md
- Release notes
- CHANGELOG.md

## Questions?

Feel free to ask questions by:
- Opening an issue with the "question" label
- Posting in the discussions section
- Reaching out to the maintainers

## Additional Notes

### Issue and Pull Request Labels

- `bug` - Something isn't working
- `enhancement` - New feature or request
- `documentation` - Improvements or additions to documentation
- `good first issue` - Good for newcomers
- `help wanted` - Extra attention is needed
- `question` - Further information is requested
- `performance` - Performance improvements
- `ui/ux` - User interface or experience improvements

---

Thank you for contributing! 🙌
