@echo off
setlocal EnableDelayedExpansion

:: first you need to git clone the project to your local folder and you need to replace it below
set "SCRIPT_PATH=D:\icloud\iCloudDrive\developer\create_project_win.py"

:: Check if Python is installed
where python >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo Python is not installed or not in PATH.
    echo Please install Python and try again.
    pause
    exit /b 1
)

:: Check if Conda is installed
where conda >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo Conda is not installed or not in PATH.
    echo Please install Conda and try again.
    pause
    exit /b 1
)

:: Initialize Conda for batch script
call conda activate base

:: Run the Python script
python "%SCRIPT_PATH%"

:: Check if the script executed successfully
if %ERRORLEVEL% neq 0 (
    echo An error occurred while running the script.
    pause
    exit /b 1
)

echo Script completed successfully!
pause
exit /b 0