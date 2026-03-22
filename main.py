import os

def create_readme():
    readme_content = """
# Tool-Selection Assistant

This tool helps agents pick the best-fit tool for a given task without drowning in options.

## Installation

No installation required. Just run the script with Python 3.

## Usage

```bash
python3 tool_selector.py --task "Your task description" --tools tool1 tool2 tool3
```

## Example

```bash
python3 tool_selector.py --task "Build a web app" --tools "Flask" "Django" "FastAPI"
```

## Running Tests

```bash
python3 test_tool_selector.py
```
"""
    with open('README.md', 'w') as f:
        f.write(readme_content)
    print("README.md created successfully.")

if __name__ == "__main__":
    create_readme()