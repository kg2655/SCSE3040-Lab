@echo off
cd /d "%~dp0"
".venv\Scripts\python.exe" -m jupyterlab --ServerApp.root_dir="%cd%" --LabApp.default_url=/lab/tree/P02-first-model/P02.ipynb
pause
