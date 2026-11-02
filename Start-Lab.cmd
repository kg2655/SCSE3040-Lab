@echo off
cd /d "%~dp0"
".venv\Scripts\python.exe" -m jupyterlab --ServerApp.root_dir="%cd%"
pause
