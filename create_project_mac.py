import os
import subprocess
import json
import sys
import shutil

# first you need to git clone the project to your local folder and you need to replace it below
BASE_DIR = os.path.expanduser("~/iCloudDrive/developer")  # Uses home directory
PYTHON_ENV_VER = "3.10"


def run_command(command):
    """
    Execute a command and handle errors.
    Args:
        command (str): Command to execute
    Returns:
        str: Command output
    """
    try:
        result = subprocess.run(command, capture_output=True, text=True, shell=True)
        if result.returncode != 0:
            print(f"Error executing command: {command}")
            print(f"Error message: {result.stderr}")
            sys.exit(1)
        return result.stdout
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        sys.exit(1)


def is_gh_installed():
    """Check if GitHub CLI is installed"""
    return shutil.which("gh") is not None


def check_prerequisites():
    """Check if required tools are installed"""
    prerequisites = {
        "python3": f"Python {PYTHON_ENV_VER}",
        "conda": "Conda",
        "git": "Git",
        "code": "Visual Studio Code"
    }
    
    missing_tools = []
    for tool, name in prerequisites.items():
        if not shutil.which(tool):
            missing_tools.append(name)
    
    if missing_tools:
        print("The following required tools are not installed or not in PATH:")
        for tool in missing_tools:
            print(f"- {tool}")
        sys.exit(1)


def create_project():
    """Main function to create a new project"""
    # Check prerequisites first
    check_prerequisites()
    
    # Get project name from user
    project_name = input("Enter the project name: ").strip()
    if not project_name:
        print("Project name cannot be empty.")
        sys.exit(1)

    # Get repository visibility from user
    while True:
        visibility = input(
            "Should the repository be public or private? (public/private): "
        ).lower().strip()
        if visibility in ["public", "private"]:
            break
        print("Invalid input. Please enter 'public' or 'private'.")

    # Set project path
    project_path = os.path.join(BASE_DIR, project_name)

    try:
        # 1. Create project folder
        os.makedirs(project_path, exist_ok=True)
        print(f"Project folder created at: {project_path}")

        # 2. Create conda environment
        print(f"Creating conda environment '{project_name}'...")
        run_command(f"conda create --name {project_name} python={PYTHON_ENV_VER} -y")
        print(f"Conda environment '{project_name}' created successfully")

        # 3. Open VSCode
        run_command(f"code {project_path}")  # Different from Windows - no shell=True needed
        print("VSCode opened")

        # 4. Initialize git and set up repository
        os.chdir(project_path)
        run_command("git init")
        run_command("git config init.defaultBranch main")
        run_command("git branch -M main")

        # 5. Create .gitignore file
        gitignore_content = """# Python
__pycache__/
*.py[cod]
*.so

# Environments
.env
.venv
env/
venv/
ENV/

# VSCode
.vscode/

# OS generated files
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db

# Distribution / packaging
dist/
build/
*.egg-info/

# Virtual environment
.env
.venv/
venv/
ENV/

# IDE specific files
.idea/
.vscode/
*.swp
*.swo

# Mac specific
.DS_Store
.AppleDouble
.LSOverride
Icon
._*
"""
        with open(os.path.join(project_path, ".gitignore"), "w") as f:
            f.write(gitignore_content)
        print(".gitignore file created")

        # Create a README.md file
        readme_content = f"""# {project_name}

## Description
This is a new project.

## Setup
1. Clone the repository
2. Create conda environment:
   ```bash
   conda create --name {project_name} python={PYTHON_ENV_VER}
   conda activate {project_name}
   ```

## Project Structure
```
{project_name}/
├── README.md
└── .gitignore
```
"""
        with open(os.path.join(project_path, "README.md"), "w") as f:
            f.write(readme_content)
        print("README.md file created")

        # Add, commit, and push
        run_command("git add .")
        run_command('git commit -m "Initial commit"')

        if is_gh_installed():
            run_command(
                f"gh repo create {project_name} --{visibility} --source=. --remote=origin"
            )
            run_command(
                f"git remote set-url origin git@github.com:Zakk-Yang/{project_name}.git"
            )
            run_command("git push -u origin main")
            print(
                f"Git repository initialized and pushed to GitHub as a {visibility} repository"
            )
        else:
            print("\nGitHub CLI (gh) is not installed. Please follow these steps to create a repository manually:")
            print(f"1. Go to https://github.com/new")
            print(f"2. Create a new repository named '{project_name}'")
            print(f"3. Set the visibility to {visibility}")
            print(f"4. Do not initialize the repository with a README, .gitignore, or license")
            print(f"5. After creating the repository, run the following commands in your project directory:")
            print(f"   git remote add origin git@github.com:Zakk-Yang/{project_name}.git")
            print(f"   git push -u origin main")

        print(f"\nProject '{project_name}' setup completed successfully!")
        print(f"\nNext steps:")
        print(f"1. Activate your conda environment: conda activate {project_name}")
        print(f"2. Start developing in VSCode!")

    except Exception as e:
        print(f"\nAn error occurred while setting up the project: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    create_project()