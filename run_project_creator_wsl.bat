@echo off
setlocal

:: first you need to git clone the project to your local folder and you need to replace it below
set SCRIPT_PATH=/mnt/c/Users/your_name/iCloudDrive/developer/auto-project-creator/create_project.py

:: Check if WSL is available
wsl.exe --status > nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo WSL is not installed or not running.
    echo Please make sure WSL is installed and running.
    pause
    exit /b 1
)

:: Run the Python script through WSL with interactive shell
wsl.exe bash -ic "python3 '%SCRIPT_PATH%'"

:: Check if the script executed successfully
if %ERRORLEVEL% neq 0 (
    echo An error occurred while running the script.
    pause
    exit /b 1
)

echo Script completed successfully!
pause
exit /b 0