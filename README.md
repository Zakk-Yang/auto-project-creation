# Auto Project Creation

This repository contains automation scripts for creating new development projects across different operating systems (Windows, Mac, and WSL). The scripts automatically set up a new project with a conda environment, Git repository, and basic project structure.

## Features

- Creates a new project directory
- Initializes a conda environment with specified Python version
- Sets up Git repository
- Creates .gitignore file with common Python ignores
- Creates initial README.md
- Opens VSCode automatically
- Creates GitHub repository (if GitHub CLI is installed)
- Cross-platform support (Windows, Mac, WSL)

## Prerequisites

- Python (3.10 or later)
- Conda package manager
- Git
- Visual Studio Code
- GitHub CLI (optional, for automatic repository creation)


## Installation

1. Clone this repository:
```bash
git clone git@github.com:Zakk-Yang/auto-project-creation.git
```

2. Choose the appropriate version for your operating system:

### Windows
- Copy `create_project_win.py` and `create_project_win.bat` to your desired location
- Edit the `BASE_DIR` in `create_project_win.py` to your preferred project directory
- Edit the `SCRIPT_PATH` in `create_project_win.bat` to point to your Python script

### Mac
- Copy `create_project_mac.py` and `create_project_mac.sh` to your desired location
- Edit the `BASE_DIR` in `create_project_mac.py` to your preferred project directory
- Make the shell script executable:
  ```bash
  chmod +x create_project_mac.sh
  ```
- Edit the `SCRIPT_PATH` in `create_project_mac.sh` to point to your Python script

### WSL
- Copy `create_project.py` and `create_project.bat` to your desired location
- Edit the `BASE_DIR` in `create_project.py` to your preferred project directory
- Edit the `SCRIPT_PATH` in `create_project.bat` to point to your Python script

## Usage

### Windows
Double-click the `create_project_win.bat` file or run it from the command prompt:
```cmd
create_project_win.bat
```

### Mac
Run the shell script:
```bash
./create_project_mac.sh
```

### WSL
Double-click the `create_project.bat` file or run it from the command prompt:
```cmd
create_project.bat
```

## Script Configuration

### Modifying Python Version
To change the Python version, edit the `PYTHON_ENV_VER` variable in the respective Python script:

```python
PYTHON_ENV_VER = "3.10"  # Change to your desired version
```

### Changing Base Directory
Edit the `BASE_DIR` variable in the respective Python script:

#### Windows
```python
BASE_DIR = "D:\\icloud\\iCloudDrive\\developer"
```

#### Mac
```python
BASE_DIR = os.path.expanduser("~/iCloudDrive/developer")
```

#### WSL
```python
BASE_DIR = "/mnt/c/Users/username/iCloudDrive/developer"
```

## Project Structure Created

Each project created will have the following structure:
```
project_name/
├── .git/
├── .gitignore
└── README.md
```

## Error Handling

The scripts include error handling for:
- Missing prerequisites
- Invalid project names
- Git initialization failures
- Conda environment creation issues
- File system operations
- GitHub repository creation errors

## Troubleshooting

### Common Issues

1. **Conda not recognized**
   - Ensure Conda is installed and in your system PATH
   - Try running `conda init` in your terminal

2. **GitHub CLI not found**
   - Install GitHub CLI or use manual repository creation
   - Run `gh auth login` to authenticate

3. **VSCode not opening**
   - Ensure VSCode is installed and in your system PATH
   - Try running `code .` in terminal to verify

4. **Git errors**
   - Ensure Git is installed and configured
   - Check if you have SSH keys set up for GitHub

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Zakk Yang

## Acknowledgments

- Inspired by the need to automate repetitive project setup tasks
- Thanks to the open-source community for various tools and inspiration

