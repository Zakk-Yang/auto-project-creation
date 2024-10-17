import os
import subprocess
import json
import sys
import shutil

# Use a Windows-style path
BASE_DIR = "D:\\icloud\\iCloudDrive\\developer"
PYTHON_ENV_VER = "3.10"


def run_command(command):
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    if result.returncode != 0:
        print(f"Error executing command: {command}")
        print(f"Error message: {result.stderr}")
        sys.exit(1)
    return result.stdout


def is_gh_installed():
    return shutil.which("gh") is not None


def create_project():
    # Get project name from user
    project_name = input("Enter the project name: ")

    # Get repository visibility from user
    while True:
        visibility = input(
            "Should the repository be public or private? (public/private): "
        ).lower()
        if visibility in ["public", "private"]:
            break
        print("Invalid input. Please enter 'public' or 'private'.")

    # Set project path
    project_path = os.path.join(BASE_DIR, project_name)

    # 1. Create project folder
    os.makedirs(project_path, exist_ok=True)
    print(f"Project folder created at: {project_path}")

    # 2. Create conda environment
    print(f"Creating conda environment '{project_name}'...")
    run_command(f"conda create --name {project_name} python={PYTHON_ENV_VER} -y")
    print(f"Conda environment '{project_name}' created successfully")

    # 3. Open VSCode
    subprocess.Popen(f"code {project_path}", shell=True)
    print("VSCode opened")

    # 4. Initialize git and set up repository
    os.chdir(project_path)
    run_command("git init")
    run_command("git config init.defaultBranch main")  # Set default branch to main
    run_command("git branch -M main")  # Rename current branch to main

    # 5. Create .gitignore file
    gitignore_content = """
# Python
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
"""
    with open(os.path.join(project_path, ".gitignore"), "w") as f:
        f.write(gitignore_content)
    print(".gitignore file created")

    # Create a README.md file
    with open(os.path.join(project_path, "README.md"), "w") as f:
        f.write(f"# {project_name}\n\nThis is a new project.")
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
        print(
            "GitHub CLI (gh) is not installed. Please follow these steps to create a repository manually:"
        )
        print(f"1. Go to https://github.com/new")
        print(f"2. Create a new repository named '{project_name}'")
        print(f"3. Set the visibility to {visibility}")
        print(
            f"4. Do not initialize the repository with a README, .gitignore, or license"
        )
        print(
            f"5. After creating the repository, run the following commands in your project directory:"
        )
        print(f"   git remote add origin git@github.com:Zakk-Yang/{project_name}.git")
        print(f"   git push -u origin main")

    print(f"Project '{project_name}' setup completed successfully!")


if __name__ == "__main__":
    create_project()
