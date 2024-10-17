# Automated Project Setup Script

This script automates the process of creating new development projects, including setting up a conda environment, initializing a git repository, and creating a GitHub repository. It's designed to work across multiple platforms: Windows (both native and using WSL), Linux, and macOS.

## Features

- Creates a new project folder
- Sets up a conda environment with a specified Python version
- Initializes a git repository
- Creates a .gitignore file and a README.md
- Opens the project in VSCode
- Creates a GitHub repository (public or private) and pushes the initial commit (if GitHub CLI is installed)

## Prerequisites

- Python 3.6+
- Conda (Miniconda or Anaconda)
- Git
- VSCode
- (Optional) GitHub CLI

## Installation

### Windows (Native)

1. Install Python: [Python for Windows](https://www.python.org/downloads/windows/)
2. Install Miniconda: [Miniconda Installation Guide](https://docs.conda.io/en/latest/miniconda.html)
3. Install Git: [Git for Windows](https://git-scm.com/download/win)
4. Install VSCode: [VSCode for Windows](https://code.visualstudio.com/download)
5. (Optional) Install GitHub CLI: [GitHub CLI for Windows](https://cli.github.com/)

### Windows (with WSL)

1. Install and set up WSL with a Linux distribution (e.g., Ubuntu).
2. In your WSL environment, install the prerequisites:
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip git
   ```
3. Install Miniconda in WSL: [Miniconda Installation Guide](https://docs.conda.io/en/latest/miniconda.html)
4. Install VSCode on Windows and ensure the "Remote - WSL" extension is installed.
5. (Optional) Install GitHub CLI in WSL:
   ```bash
   curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
   echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
   sudo apt update
   sudo apt install gh
   ```

### Linux

1. Install the prerequisites:
   ```bash
   sudo apt update  # For Debian/Ubuntu-based systems
   sudo apt install python3 python3-pip git
   ```
2. Install Miniconda: [Miniconda Installation Guide](https://docs.conda.io/en/latest/miniconda.html)
3. Install VSCode: [VSCode Installation](https://code.visualstudio.com/docs/setup/linux)
4. (Optional) Install GitHub CLI:
   ```bash
   curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
   echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
   sudo apt update
   sudo apt install gh
   ```

### macOS

1. Install Homebrew if not already installed:
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
2. Install the prerequisites:
   ```bash
   brew install python git
   ```
3. Install Miniconda: [Miniconda Installation Guide](https://docs.conda.io/en/latest/miniconda.html)
4. Install VSCode: [VSCode Installation](https://code.visualstudio.com/docs/setup/mac)
5. (Optional) Install GitHub CLI:
   ```bash
   brew install gh
   ```

## Setup

1. Clone this repository or download the script files.
2. Update the `BASE_DIR` variable in the appropriate script to your preferred project directory:
   - For Windows (Native): Update `BASE_DIR` in `create_project_win.py`
   - For other platforms: Update `BASE_DIR` in `create_project.py`

### For Windows (Native) Users

Create a batch file `run_project_creator.bat` with the following content:

```batch
@echo off
python path\to\create_project_win.py
pause
```

Replace `path\to\create_project_win.py` with the actual path to your Windows-specific Python script.

### For Windows (WSL) Users

Create a batch file `run_project_creator.bat` with the following content:

```batch
@echo off
wsl bash ~/path/to/create_project.sh
pause
```

Replace `~/path/to/create_project.sh` with the actual path to your shell script in WSL.

### For Linux and macOS Users

Make the shell script executable:

```bash
chmod +x create_project.sh
```

## Usage

### Windows (Native)

Double-click the `run_project_creator.bat` file.

### Windows (WSL)

Double-click the `run_project_creator.bat` file (different from the native Windows version).

### Linux and macOS

Run the shell script:

```bash
./create_project.sh
```

Follow the prompts to enter the project name and choose the repository visibility.

## Troubleshooting

- If conda is not recognized, ensure it's properly installed and initialized in your shell.
- If you encounter path issues, double-check the `BASE_DIR` in the appropriate Python script.
- For WSL users, ensure the paths in the batch file and shell script are correct.
- If GitHub CLI is not installed, the script will provide manual instructions for creating a GitHub repository.
- On Windows, if you encounter permission issues, try running the batch file as administrator.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE.txt file for details.

