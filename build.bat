@echo off
setlocal EnableDelayedExpansion
cd /d "%~dp0"
title VueOSD - Build

echo ==============================================
echo  VueOSD  -  Build standalone .exe
echo ==============================================
echo.

::: -- Find a usable Python -------------------------------------------------------
set PYTHON=
py --version >nul 2>&1 && set PYTHON=py
if "%PYTHON%"=="" python --version >nul 2>&1 && set PYTHON=python
if "%PYTHON%"=="" if exist "%USERPROFILE%\.workbuddy\binaries\python\versions\3.14.3\python.exe" set PYTHON="%USERPROFILE%\.workbuddy\binaries\python\versions\3.14.3\python.exe"
if "%PYTHON%"=="" if exist ".venv\Scripts\python.exe" set PYTHON=".venv\Scripts\python.exe"

if "%PYTHON%"=="" (
    echo ERROR: No Python found. Run VueOSD.bat once first to set up dependencies.
    pause
    exit /b 1
)

echo Using Python: %PYTHON%

::: -- Use venv if present (it already has the deps), else the detected Python -----
if exist ".venv\Scripts\activate.bat" (
    echo Activating .venv...
    call .venv\Scripts\activate.bat
    set PYTHON=python
)

::: -- Make sure dependencies are available ---------------------------------------
echo Checking dependencies...
%PYTHON% -c "import PyQt6, numpy, PIL" >nul 2>&1
if errorlevel 1 (
    echo Installing dependencies...
    %PYTHON% -m pip install --quiet -r requirements.txt
)

echo Installing PyInstaller...
%PYTHON% -m pip install --quiet pyinstaller

echo.
echo Building...
%PYTHON% -m PyInstaller ^
    --onefile ^
    --windowed ^
    --name "VueOSD" ^
    --add-data "fonts;fonts" ^
    --add-data "icons;icons" ^
    --add-data "assets;assets" ^
    --icon "assets\icon.ico" ^
    main.py

echo.
if exist "dist\VueOSD.exe" (
    echo [SUCCESS] dist\VueOSD.exe
    echo.
    echo Place ffmpeg.exe alongside VueOSD.exe
    echo Distribute dist\VueOSD.exe -- no Python needed on target machine.
) else (
    echo [ERROR] Build failed -- check output above.
)
pause
