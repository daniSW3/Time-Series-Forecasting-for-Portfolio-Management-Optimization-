import os
from pathlib import Path

def create_file(path, content):
    """Write content to a file, creating it if it doesn't exist."""
    with open(path, 'w') as f:
        f.write(content)

def create_project_structure(project_name):
    """Create the folder structure for a Python project."""
    # Define root directory
    root = Path(project_name)
    root.mkdir(exist_ok=True)

    # Create directories
    dirs = [
        root / 'src' / 'modules',
        root / 'src' / 'utils',
        root / 'tests',
        root / 'docs' / 'api_docs',
        root / 'scripts',
        root / 'notebooks',
        root / 'data' / 'raw',
        root / 'data' / 'processed',
        root / 'configs',
        root / '.vscode'
    ]
    for d in dirs:
        d.mkdir(parents=True, exist_ok=True)

    # .gitignore content
    gitignore_content = """__pycache__/
*.pyc
.env
/data/*
!/data/.gitkeep
.venv/
*.log
"""
    create_file(root / '.gitignore', gitignore_content)

    # requirements.txt content
    requirements_content = """python-dotenv==1.0.1
pytest==8.3.2
black==24.8.0
flake8==7.1.1
"""
    create_file(root / 'requirements.txt', requirements_content)

    # pyproject.toml content
    pyproject_content = """[project]
name = "{}"
version = "0.1.0"
dependencies = [
    "python-dotenv>=1.0.1",
    "pytest>=8.3.2",
]

[tool.black]
line-length = 88

[tool.pytest.ini_options]
minversion = "6.0"
addopts = "-ra -q"
testpaths = ["tests"]
""".format(project_name)
    create_file(root / 'pyproject.toml', pyproject_content)

    # src/main.py content
    main_content = """from modules.module1 import some_function
from utils.helper_functions import some_helper

def main():
    result = some_function()
    print(some_helper(result))

if __name__ == "__main__":
    main()
"""
    create_file(root / 'src' / 'main.py', main_content)

    # src/__init__.py (empty)
    create_file(root / 'src' / '__init__.py', '')

    # src/modules/__init__.py (empty)
    create_file(root / 'src' / 'modules' / '__init__.py', '')

    # src/modules/module1.py (sample)
    module1_content = """def some_function():
    return "Hello from module1"
"""
    create_file(root / 'src' / 'modules' / 'module1.py', module1_content)

    # src/modules/module2.py (sample)
    module2_content = """def another_function():
    return "Hello from module2"
"""
    create_file(root / 'src' / 'modules' / 'module2.py', module2_content)

    # src/utils/__init__.py (empty)
    create_file(root / 'src' / 'utils' / '__init__.py', '')

    # src/utils/helper_functions.py (sample)
    helper_content = """def some_helper(data):
    return f"Processed: {data}"
"""
    create_file(root / 'src' / 'utils' / 'helper_functions.py', helper_content)

    # tests/__init__.py (empty)
    create_file(root / 'tests' / '__init__.py', '')

    # tests/test_module1.py content
    test_module1_content = """import pytest
from src.modules.module1 import some_function

def test_some_function():
    assert some_function() == "Hello from module1"
"""
    create_file(root / 'tests' / 'test_module1.py', test_module1_content)

    # tests/test_module2.py content
    test_module2_content = """import pytest
from src.modules.module2 import another_function

def test_another_function():
    assert another_function() == "Hello from module2"
"""
    create_file(root / 'tests' / 'test_module2.py', test_module2_content)

    # docs/README.md content
    readme_content = """# {}
A Python project template.

## Setup
1. Create virtual environment: `python -m venv .venv`
2. Activate: `source .venv/bin/activate` (Linux/Mac) or `.venv\\Scripts\\activate` (Windows)
3. Install dependencies: `pip install -r requirements.txt`

## Running
Run `python src/main.py`
""".format(project_name)
    create_file(root / 'docs' / 'README.md', readme_content)

    # docs/CHANGELOG.md content
    changelog_content = """# Changelog
## [0.1.0] - {}
- Initial project setup
""".format('2025-08-08')
    create_file(root / 'docs' / 'CHANGELOG.md', changelog_content)

    # scripts/setup_dev_env.sh content
    setup_script_content = """#!/bin/bash
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
"""
    create_file(root / 'scripts' / 'setup_dev_env.sh', setup_script_content)
    # Set executable permissions for the script (Unix-like systems)
    os.chmod(root / 'scripts' / 'setup_dev_env.sh', 0o755)

    # data/.gitkeep (empty, to ensure empty data folders are tracked)
    create_file(root / 'data' / '.gitkeep', '')

    # configs/config.yaml (sample)
    config_content = """app:
  name: {}
  debug: true
""".format(project_name)
    create_file(root / 'configs' / 'config.yaml', config_content)

    # .env (sample)
    env_content = """# Environment variables
# EXAMPLE_API_KEY=your_api_key_here
"""
    create_file(root / '.env', env_content)

    # LICENSE (MIT as example)
    license_content = """MIT License

Copyright (c) 2025 Your Name

Permission is hereby granted, free of charge, to any person obtaining a copy...
"""
    create_file(root / 'LICENSE', license_content)

    # .vscode/settings.json content
    vscode_settings_content = """{
    "python.pythonPath": ".venv/bin/python",
    "python.linting.enabled": true,
    "python.linting.flake8Enabled": true,
    "python.formatting.provider": "black",
    "python.testing.pytestEnabled": true,
    "python.testing.pytestArgs": ["tests"]
}
"""
    create_file(root / '.vscode' / 'settings.json', vscode_settings_content)

    # .vscode/launch.json content
    vscode_launch_content = """{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal"
        }
    ]
}
"""
    create_file(root / '.vscode' / 'launch.json', vscode_launch_content)

    print(f"Project structure for '{project_name}' created successfully!")

if __name__ == "__main__":
    project_name = input("Enter project name: ") or "my_project"
    create_project_structure(project_name)